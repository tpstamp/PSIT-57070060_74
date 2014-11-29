def warehouse():
    wide, longth, high = input(), input(), input()
    #[wide, long, high] -- input size -> float
    amount = input()
    day_deposit = raw_input().split()   # day month year(A.D)
    time_deposit = raw_input().split()  # hour minute PM/ AM
    day_receive = raw_input().split()   
    time_receive = raw_input().split()  
    time = {'00AM':0, '01AM':1, '02AM':2, '03AM':3, '04AM':4,\
            '05AM':5, '06AM':6, '07AM':7, '08AM':8, '09AM':9,\
            '11AM':11, '12AM':12, '01PM':13, '02PM':14,\
            '03PM':15, '04PM':16, '05PM':17, '06PM':18, '07PM':19,\
            '08PM':20, '09PM':21, '10PM':22, '11PM':23}
    
    month = {'01':31, '02':29, '03':31, '04':30, '05':31, '06':30,\
             '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
    
    count = 0
    wide_t, long_t, high_t = wide*amount, longth*amount, high*amount
    if int(wide_t) != float(wide_t):
        wide_t = int(wide_t) + 1
    if int(long_t) != long_t:
        long_t = int(long_t) + 1
    while high_t >= 10:
       count += 1 
       high_t -= high * int(10 / high)
    count += 1

    
    time_n, time_d, time_allday = 0, 0, 0 
    price = 0
    if time_deposit[2] == 'PM' and time_receive[2] == 'AM'\
       and int(day_receive[0]) - int(day_deposit[0]) >= 1:
        if time[time_deposit[0]+time_deposit[2]] < 18:
            price += (((60 - float(time_deposit[1]))/60) +\
                      (17 - time[time_deposit[0]+time_deposit[2]])) * (4.5) # day
            
            price += (6 + time[time_receive[0]+time_receive[2]] +\
                      float(time_receive[1])/60) * (5.5) # night
            
            price += (int(day_receive[0]) - int(day_deposit[0]) - 1) * 120 # all day          
        else:
            price += 0 # day
            price += (23 - time[time_deposit[0]+time_deposit[2]]+\
                      ((60 - float(time_deposit[1]))/60) +\
                      time[time_receive[0]+time_receive[2]] +\
                      (float(time_receive[1])/60)) * 5.5 # night
            price += (int(day_receive[0]) - int(day_deposit[0]) - 1) * 120 # all day

            
    elif time_deposit[2] == 'AM' and time_receive[2] == 'PM'\
       and int(day_receive[0]) - int(day_deposit[0]) >= 1:

    elif time_deposit[2] == 'AM' and time_receive[2] == 'AM'\
       and int(day_receive[0]) - int(day_deposit[0]) >= 1:

    elif time_deposit[2] == 'PM' and time_receive[2] == 'PM'\
       and int(day_receive[0]) - int(day_deposit[0]) >= 1:

    

    
              
        
warehouse()

    
    
