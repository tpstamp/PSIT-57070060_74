"""
Project PSIT   : Archive Storage
Contributors   : Natcha(60)
                 Pongsathorn(74)
Language       : Python 2.7.8
GUI design IDE : Tkinter
Date modifire  : 17/12/14

__a program to calculate the warehousing costs__
input -> size and amountof product, date and time deposit, and date and time receive
output -> How much cost deposits (THB).
"""

# Import_____________________________________________________________________________________________________

from Tkinter import *
import tkMessageBox as Msgbox
from PIL import Image, ImageTk


# App________________________________________________________________________________________________________

class App:
    '''
    __main class in program__
    __init__ -> get value for this class
    textfill -> entry textvariable
    calculate -> calculate archive price form 
    reset -> reset all of value to starter value
    detail_frame -> create detail window
    detail_des -> remove detail window
    '''
    def __init__(self, main):
        '''
        Get value and create main window here
        '''
        
        # All of value
        self.wide = DoubleVar(value=0)
        self.longth = DoubleVar(value=0)
        self.high = DoubleVar(value=0)
        self.amount = IntVar(value=0)
        self.date_deposit = StringVar(value='01/01/2015')
        self.time_deposit = StringVar(value='00:00')
        self.date_receive = StringVar(value='01/01/2015')
        self.time_receive = StringVar(value='00:00')
        self.ans_price = IntVar()

        # All of getting
        self.valwide = self.textfill(self.wide)
        self.vallong = self.textfill(self.longth)
        self.valhigh = self.textfill(self.high)
        self.valamount = self.textfill(self.amount)
        self.valdate_d = self.textfill(self.date_deposit, 24)
        self.valtime_d = self.textfill(self.time_deposit, 24)
        self.valdate_r = self.textfill(self.date_receive, 24)
        self.valtime_r = self.textfill(self.time_receive, 24)
        self.valprice = self.textfill(self.ans_price)
        Button(main, font=('fantasy', 9, 'bold'), text = 'Price', command = self.calculate).place(x = 30, y = 512)
        Button(main, font=('fantasy', 9, 'bold'), text = 'Reset', command = self.reset).place(x = 280, y = 512)
        Button(main, font=('fantasy', 14, 'bold'), text = 'Detail', command = self.detail_frame).place(x = 40, y = 592)
        
        # Placr Getting
        self.valwide.place(x = 113, y = 170)
        self.vallong.place(x = 113, y = 200)
        self.valhigh.place(x = 113, y = 230)
        self.valamount.place(x = 132, y = 272)
        self.valdate_d.place(x = 105, y = 353)
        self.valtime_d.place(x = 105, y = 377)
        self.valdate_r.place(x = 105, y = 444)
        self.valtime_r.place(x = 105, y = 468)
        self.valprice.place(x = 88, y = 513)  
        
        # All of Label text
        Label(main, font=('fantasy', 7), text='Dev by NatChu, TpStamp - Dec2014').place(x = 199, y = 645)
        
    #________________________________________________________________________________________________________

    def textfill(self, all_var, side=16):
        '''
        Entry textvariable
        '''
        return Entry(main, textvariable = all_var, width = side)

    #________________________________________________________________________________________________________

    def calculate(self):
        '''
        Calculate the warehousing costs
        '''
        try:

            # Get value from window
            wide = self.wide.get()
            longth = self.longth.get()
            high = self.high.get()
            amount = self.amount.get()
            area = wide*longth
            day_deposit, month_deposit, year_deposit = map(int, self.date_deposit.get().split('/'))
            hr_deposit, min_deposit = map(int, self.time_deposit.get().split(':'))
            day_receive, month_receive, year_receive = map(int, self.date_receive.get().split('/'))
            hr_receive, min_receive = map(int, self.time_receive.get().split(':'))

            if hr_deposit == 24 and min_deposit == 0:
                hr_deposit = 0
            if hr_receive == 24 and min_receive == 0:
                hr_receive = 0
            if hr_deposit > 23 or hr_receive > 23:
                error = 0/0
                
            # Calcuate
            amount_per_column = int(10/high)
            column = float(amount) / amount_per_column
            num_column = int(column) + [0, 1][column != int(column)]
            

            month = {1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
            price = 0
                
            hm_deposit = (hr_deposit*60) + min_deposit # change hour to minute
            hm_receive = (hr_receive*60) + min_receive # change hour to minute
            md_deposit = day_deposit + month[month_deposit]
            md_receive = day_receive + month[month_receive]
            
             
            # Deposit and receive in 1 day
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
            elif hm_deposit == hm_receive:
                price += ((int(year_receive) - int(year_deposit))*43800.0) +\
                         ((md_receive - md_deposit) * 120.0)
                
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
                
                                 
            ans_price = 450 + (price * num_column * area)
            if ans_price-450 < 0 :
                error = 0/0
            
            self.valprice.delete(0, END)
            self.valprice.insert(0, '%.2f' % ans_price)
        except:
            Msgbox.showerror(title='Value Error', message='Value are Incorrect\n Please Read a Detail!!')
            self.detail_frame()

    #________________________________________________________________________________________________________

    def reset(self):
        '''reset all value'''
        self.valwide.delete(0, END)
        self.valwide.insert(0, 0)
        self.vallong.delete(0, END)
        self.vallong.insert(0, 0)
        self.valhigh.delete(0, END)
        self.valhigh.insert(0, 0)
        self.valamount.delete(0, END)
        self.valamount.insert(0, 0)
        self.valdate_d.delete(0, END)
        self.valdate_d.insert(0, '01/01/2015')
        self.valtime_d.delete(0, END)
        self.valtime_d.insert(0, '00:00')
        self.valdate_r.delete(0, END)
        self.valdate_r.insert(0, '01/01/2015')
        self.valtime_r.delete(0, END)
        self.valtime_r.insert(0, '00:00')
        self.valprice.delete(0, END)
        self.valprice.insert(0, 0)

    #________________________________________________________________________________________________________

    def detail_frame(self):
        '''this is all detail'''
        self.detail = Toplevel(main)
        self.detail.title('Detail')
        self.detail.geometry('550x440')
        self.detail.resizable(False, False)

        self.image2 = Image.open("detail.jpg")
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.detailphoto = Label(self.detail, image=self.photo2)
        self.detailphoto.image2 = self.photo2
        self.detailphoto.pack()
        
        Button(self.detail, font=('fantasy', 16, 'bold'), text = 'Agree..!!', command = self.detail_des).place(x = 380, y = 366)

    #________________________________________________________________________________________________________
        
    def detail_des(self):
        '''destroy a detail'''
        self.detail.destroy()



# Main loop__________________________________________________________________________________________________

main = Tk()
text = Text()
text.config(font=('courier', 15, 'normal'))
main.title('Archive Store')
main.geometry('360x660')
main.resizable(False, False)

image = Image.open("home.jpg")
photo = ImageTk.PhotoImage(image)
mainphoto = Label(image=photo)
mainphoto.image = photo
mainphoto.pack()


mainGUI = App(main)
main.mainloop()

# End________________________________________________________________________________________________________
