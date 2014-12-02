def warehouse():
    wide, longth, high = input(), input(), input()
    #[wide, long, high] -- input size -> float
    amount = input()
    day_deposit = raw_input().split()   # day month year(A.D)
    time_deposit = raw_input().split()  # 00:00 - 24:00
    day_receive = raw_input().split()   
    time_receive = raw_input().split()  
    month = {'01':0, '02':31, '03':59, '04':90, '05':120, '06':151,\
             '07':181, '08':212, '09':243, '10':273, '11':304, '12':334}
    
    area = wide*longth
    amount_per_column = int(10/high)
    num_column = int(amount / amount_per_column)
    if amount / amount_per_column != int(amount / amount_per_column):
        num_column += 1

    
    price = 0
    hm_deposit = (int(time_deposit[0])*60) + int(time_deposit[1]) # change hour to minute
    hm_receive = (int(time_receive[0])*60) + int(time_receive[1]) # change hour to minute
    md_deposit = int(day_deposit[0]) + month[day_deposit[1]]
    md_receive = int(day_receive[0]) + month[day_receive[1]]
    # deposit and receive in 1 day
    if day_deposit[0] == day_receive[0] and\
       day_deposit[1] == day_receive[1] and\
       day_deposit[2] == day_receive[2]:
        if hm_deposit >= 0 and hm_deposit <= 360:
            price += (360 - hm_deposit)/60.0 * 5.5
            if hm_receive >= 0 and hm_receive <= 360:
                price -= (360 - hm_receive)/60.0 * 5.5
            elif hm_receive > 360 and hm_receive <= 1080:
                price += (hm_receive - 360)/60.0 * 4.5
            elif hm_receive >= 1080 and hm_receive <= 1440:
                price += (720/60.0 * 4.5) + ((hm_receive - 1080)/60.0 * 5.5)
        elif hm_deposit > 360 and hm_deposit <= 1080:
            price += (1080 - hm_deposit)/60.0 * 4.5
            if hm_receive > 360 and hm_receive <= 1080:
                price -= (1080 - hm_receive)/60.0 * 4.5
            elif hm_receive >= 1080 and hm_receive <= 1440:
                price += (1440 - hm_receive)/60.0 * 5.5
        elif hm_deposit > 1080 and hm_deposit <= 1440:
            price += (1440 - hm_deposit)/60.0 * 5.5
            if hm_receive >= 1080 and hm_receive <= 1440:
                price -= (1440 - hm_receive)/60.0 * 5.5

    
    # deposit and receive more 1 day    
    # deposit
    else:
        if hm_deposit >= 0 and hm_deposit <= 360:
            price += ((360 - hm_deposit)/60.0 * 5.5) + (12 * 4.5) + (6 * 5.5)
        elif hm_deposit > 360 and hm_deposit <= 1080:
            price += ((1080 - hm_deposit)/60.0 * 4.5) + (6 * 5.5)
        elif hm_deposit > 1080 and hm_deposit <= 1440:
            price += (1440 - hm_deposit)/60.0 * 5.5
                            
    # check day, month, year
        if int(day_receive[2]) - int(day_deposit[2]) >= 1:
            price += ((365 - md_deposit - 1) * 120) +\
                     (int(day_receive[2]) - int(day_deposit[2] - 1)*43800) +\
                     (md_receive * 120)
        elif int(day_receive[2]) - int(day_deposit[2]) == 0:
            price += (md_receive - md_deposit - 2) * 120
    # receive
        if hm_receive >= 0 and hm_receive <= 360:
            price += hm_receive/60.0 * 5.5
        elif hm_receive > 360 and hm_receive <= 1080:
            price += (6*5.5) + ((hm_receive - 360)/60.0 * 4.5)
        elif hm_receive > 1080 and hm_receive <= 1440:
            price += (6*5.5) + (12*4.5) + ((hm_receive - 1080)/60.0 * 5.5)       
    print price * num_column * area
   
warehouse()
    
