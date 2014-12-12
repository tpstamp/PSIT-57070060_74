"""
Project PSIT   : Archive Store
Contributors   : Natcha(60)
                 Pongsathorn(74)
Language       : Python 2.7.8
GUI design IDE : Tkinter
Date modifire  : 9/12/14

"""

from Tkinter import *
import tkMessageBox as Msgbox

class App:
    '''
    main func in this program
    __init__ -> get value for this class
    textfill -> entry textvariable
    calculate -> calculate archive price form 
    reset -> reset all of value to starter value
    '''
    def __init__(self, main):
        '''
        Edit GUI Here
        '''

        # All of value
        self.wide = IntVar(value=1)
        self.longth = IntVar(value=1)
        self.high = IntVar(value=1)
        self.amount = IntVar(value=1)
        self.date_deposit = StringVar(value='01/01/2014')
        self.time_deposit = StringVar(value='00:00')
        self.date_receive = StringVar(value='01/01/2014')
        self.time_receive = StringVar(value='00:00')
        self.ans_price = IntVar()

        # All of getting
        self.valwide = self.textfill(self.wide)
        self.vallong = self.textfill(self.longth)
        self.valhigh = self.textfill(self.high)
        self.valamount = self.textfill(self.amount)
        self.valdate_d = self.textfill(self.date_deposit)
        self.valtime_d = self.textfill(self.time_deposit)
        self.valdate_r = self.textfill(self.date_receive)
        self.valtime_r = self.textfill(self.time_receive)
        self.valprice = self.textfill(self.ans_price)
        Button(main, text = 'Price', command = self.calculate).place(x = 20, y = 290)
        Button(main, text = 'Reset', command = self.reset).place(x = 240, y = 290)

        # Placr Getting
        self.valwide.place(x = 100, y = 50)
        self.vallong.place(x = 100, y = 80)
        self.valhigh.place(x = 100, y = 110)
        self.valamount.place(x = 100, y = 140)
        self.valdate_d.place(x = 100, y = 170)
        self.valtime_d.place(x = 100, y = 200)
        self.valdate_r.place(x = 100, y = 230)
        self.valtime_r.place(x = 100, y = 260)
        self.valprice.place(x = 65, y = 294)
        
        # All of Label text
        Label(main, text = 'Archive Store').pack()
        Label(main, text='Wide     :').place(x = 20, y = 50)
        Label(main, text='Metre').place(x = 230, y = 50)
        Label(main, text='Long     :').place(x = 20, y = 80)
        Label(main, text='Metre').place(x = 230, y = 80)
        Label(main, text='High     :').place(x = 20, y = 110)
        Label(main, text='Metre').place(x = 230, y = 110)
        Label(main, text='Amount   :').place(x = 20, y = 140)
        Label(main, text='Piece(s)').place(x = 230, y = 140)
        Label(main, text='Day dep  :').place(x = 20, y = 170)
        Label(main, text='Time dep :').place(x = 20, y = 200)
        Label(main, text='Day rec  :').place(x = 20, y = 230)
        Label(main, text='Time rec :').place(x = 20, y = 260)
        Label(main, text='Baht(s)').place(x = 195, y = 294)
        Label(main, text='*price rate : day 4.5baht/metre/hour\n             night 5.5 baht/metre/hour').place(x = 100, y = 320)
        
        
    def textfill(self, all_var):
        '''entry textvariable'''
        return Entry(main, textvariable = all_var)

    def calculate(self):
        '''
        calculate price of archive
        '''
        wide = self.wide.get()
        longth = self.longth.get()
        high = self.high.get()
        amount = self.amount.get()
        area = wide*longth

        # day month year(A.D) deposit
        day_deposit, month_deposit, year_deposit = map(int, self.date_deposit.get().split('/'))
        
        # time deposit 00:00 - 24:00
        hr_deposit, min_deposit = map(int, self.time_deposit.get().split(':'))
        
        # day month year(A.D) receive
        day_receive, month_receive, year_receive = map(int, self.date_receive.get().split('/'))
                                                       
        # time receive 00:00 - 23:59
        hr_receive, min_receive = map(int, self.time_receive.get().split(':'))
        
    
        amount_per_column = int(10/high)
        num_column = int(amount / amount_per_column)
        if amount / amount_per_column != int(amount / amount_per_column):
            num_column += 1

        month = {   1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
        price = 0
                
        hm_deposit = (hr_deposit*60) + min_deposit # change hour to minute
        hm_receive = (hr_receive*60) + min_receive # change hour to minute
        md_deposit = day_deposit + month[month_deposit]
        md_receive = day_receive + month[month_receive]
                
        # deposit and receive in 1 day
        if day_deposit == day_receive and\
           month_deposit == month_receive and\
           year_deposit == year_receive:
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
            if int(year_receive) - int(year_deposit) >= 1:
                price += ((365 - md_deposit - 1) * 120) +\
                         (int(year_receive) - int(year_deposit - 1)*43800) +\
                         (md_receive * 120)
            elif int(year_receive) - int(year_deposit) == 0:
                price += (md_receive - md_deposit - 2) * 120
        # receive
            if hm_receive >= 0 and hm_receive <= 360:
                price += hm_receive/60.0 * 5.5
            elif hm_receive > 360 and hm_receive <= 1080:
                price += (6*5.5) + ((hm_receive - 360)/60.0 * 4.5)
            elif hm_receive > 1080 and hm_receive <= 1440:
                price += (6*5.5) + (12*4.5) + ((hm_receive - 1080)/60.0 * 5.5)
                                      
        ans_price = price * num_column * area
        
        self.valprice.delete(0, END)
        self.valprice.insert(0, ans_price)                         
        
    def reset(self):
        '''reset all value'''
        self.valwide.delete(0, END)
        self.valwide.insert(0, 1)
        self.vallong.delete(0, END)
        self.vallong.insert(0, 1)
        self.valhigh.delete(0, END)
        self.valhigh.insert(0, 1)
        self.valamount.delete(0, END)
        self.valamount.insert(0, 1)
        self.valdate_d.delete(0, END)
        self.valdate_d.insert(0, '01/01/2014')
        self.valtime_d.delete(0, END)
        self.valtime_d.insert(0, '00:00')
        self.valdate_r.delete(0, END)
        self.valdate_r.insert(0, '01/01/2014')
        self.valtime_r.delete(0, END)
        self.valtime_r.insert(0, '00:00')
        self.valprice.delete(0, END)
        self.valprice.insert(0, 0)  


main = Tk()
main.title('Archive Store')
main.geometry('300x360')
mainGUI = App(main)
main.mainloop()

        
        

