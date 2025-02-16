from PIL import Image, ImageFilter
from tkinter import *
import tkinter
from tkinter import ttk  
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import webbrowser
#from tkinter import ttk
#from tkinter import scrolledtext
#from tkinter.ttk import *
import time
import tkinter as tk
from tkinter import Tk
from datetime import datetime
import pytz
import os
import mysql.connector
from mysql.connector import Error
from copy import copy

#############################################################################################################################
def openWithdraw():
    rootwithdraw=Toplevel()
    rootwithdraw.title("WITHDRAW")
    rootwithdraw.geometry('1920x1080')
    
 
    def withdraw(text):
        new_withdraw.insert("end", text)
        if(int(new_withdraw.get())>=100):
            ok.configure(state="normal")

    def withdraw_action():
        with_balance= ("SELECT balance from card_details where Acc_No="+acc_entry.get())
        mycursor.execute(with_balance)
        result= mycursor.fetchone()

        for row in result:
            print(row)

        i=int(row)
        if(i>=int((int(new_withdraw.get())+2000))):
           i=i-int((new_withdraw.get()))
           updated_bal= ("UPDATE card_details SET balance=%i  WHERE Acc_No=%i" % (int(i),int(acc_entry.get())))
           mycursor.execute(updated_bal)
           mydb.commit()
           print(mycursor.rowcount, "record(s) affected")
           messagebox.showinfo("TRANSACTION SUCCESSFUL", "YOUR TRANSACTION HAS BEEN COMPLETED SUCCESSFULLY!")
           openDashboard()

        else:
            messagebox.showerror("TRANSACTION FAILED", "WE ARE SORRY, BUT YOU HAVE INSUFFICIENT WITHDRAWAL BALANCE...")
            openDashboard()
      
        
        
    #Frame1 and its details
    frame1 = tk.LabelFrame(rootwithdraw,bg="white", highlightbackground="white", highlightthickness="3")
    frame1.place(x=0, y=0, width=1280, height=120)

    logo= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
    logoref=logo
    label=ttk.Label(frame1, image=logoref)
    label.image=logoref
    label.place(x=-30, y=-30, width=60, height=60)


    title1=Label(frame1, text="QUERENCIA", bg="white", fg="black", font=("times new roman", 25, "bold"))
    title1.place(x=40, y=30)
    title2=Label(frame1, text="Toll free: 0900-0723-0213", bg="white", fg="black", font=("times new roman", 10))
    title2.place(x=45, y=70)


    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #Frame2 and its details

    frame2 = tk.LabelFrame(rootwithdraw,bg="black", highlightbackground="white", highlightthickness="3" )
    frame2.place(x=0, y=120, width=640, height=1160)


    head1=Label(frame2, text="CASH WITHDRAW", bg="black", fg="#00B9FF", font=("times new roman", 20, "bold"))
    head1.place(x=200, y=30)


    # Load the image
    pin1=Image.open('D:/College/BE project/proj final/Images/withdraw.png')

    # Resize the image in the given (width, height)
    p1=pin1.resize((90, 90))

    # Conver the image in TkImage
    my_pin1=ImageTk.PhotoImage(p1)
    mypin1ref=my_pin1

    # Display the image with label
    label=Label(frame2, image=mypin1ref)
    label.image=mypin1ref
    label.pack()
    label.place(x=275, y=110)


    head2=Label(frame2, text="Enter the amount to be withdrawn:", bg="black", fg="#00B9FF", font=("times new roman", 18, "bold"))
    head2.place(x=50, y=290)
    new_withdraw= Entry(frame2, width=10, bg="#797D7F", fg="white", font=("calibri", 15, "bold"))
    new_withdraw.place(x=450, y=290)

    back=tk.Button(frame2, text="Back", font=('Helvetica','20'), command=openDashboard)
    back.place(x=275, y=450, width=90, height=50)
    back.configure(bg="white", fg="#00B9FF")

        
    #Frame3 and its details
   

    frame3 = tk.LabelFrame(rootwithdraw,bg="#797D7F", highlightbackground="#00B9FF", highlightthickness="3")
    frame3.place(x=640, y=120, width=640, height=1160)

    one=tk.Button(frame3, text="1", font=('Helvetica','40', "bold"), command=lambda:withdraw("1"))
    one.place(x=180, y=50, width=60, height=60)
    one.configure(bg="white", fg="#242728")

    two=tk.Button(frame3, text="2", font=('Helvetica','40', "bold"), command=lambda:withdraw("2"))
    two.place(x=280, y=50, width=60, height=60)
    two.configure(bg="white", fg="#242728")

    three=tk.Button(frame3, text="3", font=('Helvetica','40', "bold"), command=lambda:withdraw("3"))
    three.place(x=380, y=50, width=60, height=60)
    three.configure(bg="white", fg="#242728")

    four=tk.Button(frame3, text="4", font=('Helvetica','40', "bold"), command=lambda:withdraw("4"))
    four.place(x=180, y=150, width=60, height=60)
    four.configure(bg="white", fg="#242728")

    five=tk.Button(frame3, text="5", font=('Helvetica','40', "bold"), command=lambda:withdraw("5"))
    five.place(x=280, y=150, width=60, height=60)
    five.configure(bg="white", fg="#242728")

    six=tk.Button(frame3, text="6", font=('Helvetica','40', "bold"), command=lambda:withdraw("6"))
    six.place(x=380, y=150, width=60, height=60)
    six.configure(bg="white", fg="#242728")

    seven=tk.Button(frame3, text="7", font=('Helvetica','40', "bold"), command=lambda:withdraw("7"))
    seven.place(x=180, y=250, width=60, height=60)
    seven.configure(bg="white", fg="#242728")

    eight=tk.Button(frame3, text="8", font=('Helvetica','40', "bold"), command=lambda:withdraw("8"))
    eight.place(x=280, y=250, width=60, height=60)
    eight.configure(bg="white", fg="#242728")

    nine=tk.Button(frame3, text="9", font=('Helvetica','40', "bold"), command=lambda:withdraw("9"))
    nine.place(x=380, y=250, width=60, height=60)
    nine.configure(bg="white", fg="#242728")

    doublezero=tk.Button(frame3, text="00", font=('Helvetica','40', "bold"), command=lambda:withdraw("00"))
    doublezero.place(x=180, y=350, width=60, height=60)
    doublezero.configure(bg="white", fg="#242728")

    zero=tk.Button(frame3, text="0", font=('Helvetica','40', "bold"), command=lambda:withdraw("0"))
    zero.place(x=280, y=350, width=60, height=60)
    zero.configure(bg="white", fg="#242728")

   
    # Load the image
    cross1=Image.open('D:/College/BE project/proj final/Images/cross.png')

    # Resize the image in the given (width, height)
    cro1=cross1.resize((55, 55))

    # Conver the image in TkImage
    my_cross1=ImageTk.PhotoImage(cro1)
    mycross1ref=my_cross1

    # Display the image with label
    label=Label(frame3, image=mycross1ref)
    label.image=mycross1ref
    label.pack()
    label.place(x=380, y=350)

    back_btn=tk.Button(frame3, image=mycross1ref, font=('Helvetica','40', "bold"), command=clear)
    back_btn.place(x=380, y=350, width=60, height=60)
    back_btn.configure(bg="white", fg="#242728")

    ok=tk.Button(frame3, text="Proceed", font=('Helvetica','20'), state="disabled", command=openAuthentication)
    ok.place(x=240, y=450, width=150, height=50)
    ok.configure(bg="#242728", fg="#00B9FF")

    

#####################################################################################################################################

def openDeposit():
    rootwithdraw=Toplevel()
    rootwithdraw.title("DEPOSIT")
    rootwithdraw.geometry('1920x1080')

    def deposit(text):
        new_deposit.insert("end", text)
        if(int(new_deposit.get())>=100):
            ok.configure(state="normal")

    def deposit_action():
        with_balance= ("SELECT balance from card_details where Acc_No="+acc_entry.get())
        mycursor.execute(with_balance)
        result= mycursor.fetchone()

        for row in result:
            print(row)

        j=int(row)
        if(j>=2000):
           j=j+int((new_deposit.get()))
           updated_bal= ("UPDATE card_details SET balance=%i  WHERE Acc_No=%i" % (int(j),int(acc_entry.get())))
           mycursor.execute(updated_bal)
           mydb.commit()
           print(mycursor.rowcount, "record(s) affected")
           messagebox.showinfo("TRANSACTION SUCCESSFUL", "YOUR TRANSACTION HAS BEEN COMPLETED SUCCESSFULLY!")
           openDashboard()

        else:
            messagebox.showerror("TRANSACTION FAILED", "WE ARE SORRY, BUT YOU HAVE INSUFFICIENT WITHDRAWAL BALANCE...")
            openDashboard()


    #Frame1 and its details
    frame1 = tk.LabelFrame(rootwithdraw,bg="white", highlightbackground="white", highlightthickness="3")
    frame1.place(x=0, y=0, width=1280, height=120)

    logo= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
    logoref=logo
    label=ttk.Label(frame1, image=logoref)
    label.image=logoref
    label.place(x=-30, y=-30, width=60, height=60)


    title1=Label(frame1, text="QUERENCIA", bg="white", fg="black", font=("times new roman", 25, "bold")).place(x=40, y=30)
    title2=Label(frame1, text="Toll free: 0900-0723-0213", bg="white", fg="black", font=("times new roman", 10)).place(x=45, y=70)


    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #Frame2 and its details

    frame2 = tk.LabelFrame(rootwithdraw,bg="black", highlightbackground="white", highlightthickness="3" )
    frame2.place(x=0, y=120, width=640, height=1160)


    head1=Label(frame2, text="CASH DEPOSIT", bg="black", fg="#00B9FF", font=("times new roman", 20, "bold")).place(x=200, y=30)


    # Load the image
    pin1=Image.open('D:/College/BE project/proj final/Images/withdraw.png')

    # Resize the image in the given (width, height)
    p1=pin1.resize((90, 90))

    # Conver the image in TkImage
    my_pin1=ImageTk.PhotoImage(p1)
    mypin1ref=my_pin1

    # Display the image with label
    label=Label(frame2, image=mypin1ref)
    label.image=mypin1ref
    label.pack()
    label.place(x=275, y=110)


    head2=Label(frame2, text="Enter the amount to be deposited:", bg="black", fg="#00B9FF", font=("times new roman", 18, "bold")).place(x=50, y=290)
    new_deposit= Entry(frame2, width=10, bg="#797D7F", fg="white", font=("calibri", 15, "bold"))
    new_deposit.place(x=450, y=290)



    back=tk.Button(frame2, text="Back", font=('Helvetica','20'), command=openDashboard)
    back.place(x=275, y=450, width=90, height=50)
    back.configure(bg="white", fg="#00B9FF")



    #Frame3 and its details

    frame3 = tk.LabelFrame(rootwithdraw,bg="#797D7F", highlightbackground="#00B9FF", highlightthickness="3")
    frame3.place(x=640, y=120, width=640, height=1160)

    one=tk.Button(frame3, text="1", font=('Helvetica','40', "bold"), command=lambda:deposit("1"))
    one.place(x=180, y=50, width=60, height=60)
    one.configure(bg="white", fg="#242728")

    two=tk.Button(frame3, text="2", font=('Helvetica','40', "bold"), command=lambda:deposit("2"))
    two.place(x=280, y=50, width=60, height=60)
    two.configure(bg="white", fg="#242728")

    three=tk.Button(frame3, text="3", font=('Helvetica','40', "bold"), command=lambda:deposit("3"))
    three.place(x=380, y=50, width=60, height=60)
    three.configure(bg="white", fg="#242728")

    four=tk.Button(frame3, text="4", font=('Helvetica','40', "bold"), command=lambda:deposit("4"))
    four.place(x=180, y=150, width=60, height=60)
    four.configure(bg="white", fg="#242728")

    five=tk.Button(frame3, text="5", font=('Helvetica','40', "bold"), command=lambda:deposit("5"))
    five.place(x=280, y=150, width=60, height=60)
    five.configure(bg="white", fg="#242728")

    six=tk.Button(frame3, text="6", font=('Helvetica','40', "bold"), command=lambda:deposit("6"))
    six.place(x=380, y=150, width=60, height=60)
    six.configure(bg="white", fg="#242728")

    seven=tk.Button(frame3, text="7", font=('Helvetica','40', "bold"), command=lambda:deposit("7"))
    seven.place(x=180, y=250, width=60, height=60)
    seven.configure(bg="white", fg="#242728")

    eight=tk.Button(frame3, text="8", font=('Helvetica','40', "bold"), command=lambda:deposit("8"))
    eight.place(x=280, y=250, width=60, height=60)
    eight.configure(bg="white", fg="#242728")

    nine=tk.Button(frame3, text="9", font=('Helvetica','40', "bold"), command=lambda:deposit("9"))
    nine.place(x=380, y=250, width=60, height=60)
    nine.configure(bg="white", fg="#242728")

    doublezero=tk.Button(frame3, text="00", font=('Helvetica','40', "bold"), command=lambda:deposit("00"))
    doublezero.place(x=180, y=350, width=60, height=60)
    doublezero.configure(bg="white", fg="#242728")

    zero=tk.Button(frame3, text="0", font=('Helvetica','40', "bold"),command=lambda:deposit("0"))
    zero.place(x=280, y=350, width=60, height=60)
    zero.configure(bg="white", fg="#242728")



    # Load the image
    cross1=Image.open('D:/College/BE project/proj final/Images/cross.png')

    # Resize the image in the given (width, height)
    cro1=cross1.resize((55, 55))

    # Conver the image in TkImage
    my_cross1=ImageTk.PhotoImage(cro1)
    mycross1ref=my_cross1

    # Display the image with label
    label=Label(frame3, image=mycross1ref)
    label.image=mycross1ref
    label.pack()
    label.place(x=380, y=350)

    back=tk.Button(frame3, image=mycross1ref, font=('Helvetica','40', "bold"))
    back.place(x=380, y=350, width=60, height=60)
    back.configure(bg="white", fg="#242728")

    ok=tk.Button(frame3, text="Proceed", font=('Helvetica','20'), state="disabled", command=openAuthentication)
    ok.place(x=240, y=450, width=150, height=50)
    ok.configure(bg="#242728", fg="#00B9FF")


#####################################################################################################################################

def viewBalance():
    rootbalance=Toplevel()
    rootbalance.title("BALANCE")
    rootbalance.geometry('1920x1080')


    #Frame1 and its details
    frame1 = tk.LabelFrame(rootbalance,bg="white", highlightbackground="white", highlightthickness="3")
    frame1.place(x=0, y=0, width=1280, height=120)

    logobal= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
    logobalref=logobal
    label=ttk.Label(frame1, image=logobalref)
    label.image=logobalref
    label.place(x=-30, y=-30, width=60, height=60)


    title1=Label(frame1, text="QUERENCIA", bg="white", fg="black", font=("times new roman", 25, "bold")).place(x=40, y=30)
    title2=Label(frame1, text="Toll free: 0900-0723-0213", bg="white", fg="black", font=("times new roman", 10)).place(x=45, y=70)


    #Frame2 and its details

    frame2 = tk.LabelFrame(rootbalance,bg="black", highlightbackground='white', highlightthickness="3")
    frame2.place(x=0, y=120, width=1280, height=1120)


    # Load the image
    image1=Image.open('D:/College/BE project/proj final/Images/rupee.png')

    # Resize the image in the given (width, height)
    img1=image1.resize((100, 100))

    # Conver the image in TkImage
    my_img1=ImageTk.PhotoImage(img1)
    img1ref=my_img1

    # Display the image with label
    label=Label(frame2, image=img1ref)
    label.image=img1ref
    label.pack()
    label.place(x=560, y=100)



    bal1=Label(frame2, text="Your current account balance:", bg="black", fg="#00B9FF", font=("times new roman", 20, "bold")).place(x=380, y=270)
    bal1_current=Label(frame2, text="Rs. ", bg="black", fg="white", font=("times new roman", 20, "bold")).place(x=770, y=270)
    disp_balance= "SELECT balance from card_details where Acc_No="+acc_entry.get()
    mycursor.execute(disp_balance)
    result= mycursor.fetchone()
    for row in result:
        print(row)
        bal=StringVar()
        bal.set(row)
        
        label_currentbal= Label(frame2, textvariable=bal, bg="black", fg="white", font=("times new roman", 20, "bold")).place(x=810, y=270)
        
    bal2=Label(frame2, text="Balance available for withdrawal:", bg="black", fg="#00B9FF", font=("times new roman", 20, "bold")).place(x=340, y=330)
    bal2_available=Label(frame2, text="Rs. ", bg="black", fg="white", font=("times new roman", 20, "bold")).place(x=770, y=330)
    for row in result:
        row=int(row)-2000
        avail=StringVar()
        avail.set(row)
        
    label_availablebal= Label(frame2, textvariable=avail, bg="black", fg="white", font=("times new roman", 20, "bold")).place(x=810, y=330)

    back_to_dash=tk.Button(frame2, text="Back to Dashboard", font=('Helvetica','15', "bold"), command=openDashboard)
    back_to_dash.place(x=508, y=430, width=200, height=50)
    back_to_dash.configure(bg="#242728", fg="#00B9FF")


######################################################################################################################################
pincount=0
repincount=0
new_pin_final=0
reset_new_pin_final=0

def pinChange():
    rootpin=Toplevel()
    rootpin.title("CHANGE PIN")
    rootpin.geometry('1920x1080')


     #Frame1 and its details
    frame1 = tk.LabelFrame(rootpin,bg="white", highlightbackground="white", highlightthickness="3")
    frame1.place(x=0, y=0, width=1280, height=120)

    logopin= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
    logopinref=logopin
    label=ttk.Label(frame1, image=logopinref)
    label.image=logopinref
    label.place(x=-30, y=-30, width=60, height=60)


    title1=Label(frame1, text="QUERENCIA", bg="white", fg="black", font=("times new roman", 25, "bold")).place(x=40, y=30)
    title2=Label(frame1, text="Toll free: 0900-0723-0213", bg="white", fg="black", font=("times new roman", 10)).place(x=45, y=70)


    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #Frame2 and its details

    frame2 = tk.LabelFrame(rootpin,bg="black", highlightbackground="white", highlightthickness="3" )
    frame2.place(x=0, y=120, width=640, height=1160)


    head1=Label(frame2, text="Change PIN", bg="black", fg="#00B9FF", font=("times new roman", 20, "bold")).place(x=225, y=30)


    # Load the image
    pin1=Image.open('D:/College/BE project/proj final/Images/lock.png')

    # Resize the image in the given (width, height)
    p1=pin1.resize((90, 90))

    # Conver the image in TkImage
    my_pin1=ImageTk.PhotoImage(p1)
    pin1ref=my_pin1

    # Display the image with label
    label=Label(frame2, image=pin1ref)
    label.image=pin1ref
    label.pack()
    label.place(x=255, y=110)


    head2=Label(frame2, text="Enter new PIN:", bg="black", fg="#00B9FF", font=("times new roman", 18, "bold")).place(x=130, y=290)
    new_pin= Entry(frame2, width=5, bg="#797D7F", fg="white", font=("calibri", 15, "bold"), show="*")
    new_pin.place(x=350, y=290)
    head3=Label(frame2, text="Re-enter new PIN:", bg="black", fg="#00B9FF", font=("times new roman", 18, "bold")).place(x=100, y=370)
    reenter_new_pin= Entry(frame2, width=5, bg="#797D7F", fg="white", font=("calibri", 15, "bold"), show="*")
    reenter_new_pin.place(x=350, y=370)

    back2=tk.Button(frame2, text="Back", font=('Helvetica','20'), command=openDashboard)
    back2.place(x=260, y=450, width=90, height=50)
    back2.configure(bg="white", fg="#00B9FF")


    #Frame3 and its details
        

    frame3 = tk.LabelFrame(rootpin,bg="#797D7F", highlightbackground="#00B9FF", highlightthickness="3")
    frame3.place(x=640, y=120, width=640, height=1160)

    one=tk.Button(frame3, text="1", font=('Helvetica','40', "bold"), command=lambda:change_pin("1"))
    one.place(x=180, y=50, width=60, height=60)
    one.configure(bg="white", fg="#242728")

    two=tk.Button(frame3, text="2", font=('Helvetica','40', "bold"), command=lambda:change_pin("2"))
    two.place(x=280, y=50, width=60, height=60)
    two.configure(bg="white", fg="#242728")

    three=tk.Button(frame3, text="3", font=('Helvetica','40', "bold"), command=lambda:change_pin("3"))
    three.place(x=380, y=50, width=60, height=60)
    three.configure(bg="white", fg="#242728")

    four=tk.Button(frame3, text="4", font=('Helvetica','40', "bold"), command=lambda:change_pin("4"))
    four.place(x=180, y=150, width=60, height=60)
    four.configure(bg="white", fg="#242728")

    five=tk.Button(frame3, text="5", font=('Helvetica','40', "bold"), command=lambda:change_pin("5"))
    five.place(x=280, y=150, width=60, height=60)
    five.configure(bg="white", fg="#242728")

    six=tk.Button(frame3, text="6", font=('Helvetica','40', "bold"), command=lambda:change_pin("6"))
    six.place(x=380, y=150, width=60, height=60)
    six.configure(bg="white", fg="#242728")

    seven=tk.Button(frame3, text="7", font=('Helvetica','40', "bold"), command=lambda:change_pin("7"))
    seven.place(x=180, y=250, width=60, height=60)
    seven.configure(bg="white", fg="#242728")

    eight=tk.Button(frame3, text="8", font=('Helvetica','40', "bold"), command=lambda:change_pin("8"))
    eight.place(x=280, y=250, width=60, height=60)
    eight.configure(bg="white", fg="#242728")

    nine=tk.Button(frame3, text="9", font=('Helvetica','40', "bold"), command=lambda:change_pin("9"))
    nine.place(x=380, y=250, width=60, height=60)
    nine.configure(bg="white", fg="#242728")

    doublezero=tk.Button(frame3, text="00", font=('Helvetica','40', "bold"), command=lambda:change_pin("00"))
    doublezero.place(x=180, y=350, width=60, height=60)
    doublezero.configure(bg="white", fg="#242728")

    zero=tk.Button(frame3, text="0", font=('Helvetica','40', "bold"), command=lambda:change_pin("0"))
    zero.place(x=280, y=350, width=60, height=60)
    zero.configure(bg="white", fg="#242728")


    # Load the image
    cross1=Image.open('D:/College/BE project/proj final/Images/cross.png')

    # Resize the image in the given (width, height)
    cro1=cross1.resize((55, 55))

    # Conver the image in TkImage
    my_cross1=ImageTk.PhotoImage(cro1)
    cross1ref=my_cross1

    # Display the image with label
    label=Label(frame3, image=cross1ref)
    label.image=cross1ref
    label.pack()
    label.place(x=380, y=350)

    back=tk.Button(frame3, image=cross1ref, font=('Helvetica','40', "bold"))
    back.place(x=380, y=350, width=60, height=60)
    back.configure(bg="#044D72", fg="#242728")

    ok=tk.Button(frame3, text="Reset PIN", font=('Helvetica','20'), command=pin_compare, state="disabled")
    ok.place(x=240, y=450, width=150, height=50)
    ok.configure(bg="#242728", fg="#00B9FF")

    def change_pin(text):
        global pincount
        global repincount
        global new_pin_final
        global reset_new_pin_final

        if(text=="00" and pincount>=3):
            return 0

        elif(text=="00" and pincount<=2):
            new_pin.insert("end",text)
            pincount = pincount+2
            if(pincount==4):
                new_pin.config(state="disabled")

        elif(pincount<=3):
            new_pin.insert("end",text)
            pincount = pincount+1
            if(pincount==4):
                new_pin.config(state="disabled")
                print(repincount)
        
        elif(pincount>=4):
            if(text=="00" and repincount>=3):
                return 0
                

            elif(text=="00" and repincount<=2):
                reenter_new_pin.insert("end",text)
                repincount = repincount+2
                if(repincount==4):
                    reenter_new_pin.config(state="disabled")

            elif(repincount<=3):
                reenter_new_pin.insert("end",text)
                repincount = repincount+1
                if(repincount==4):
                    reenter_new_pin.config(state="disabled")
                    new_pin_final=(new_pin.get())
                    print(new_pin_final)
                    reset_new_pin_final=(reenter_new_pin.get())
                    print(reset_new_pin_final)
                    
                    ok.configure(state="normal")
                  

def pin_compare():
    global new_pin_final
    global reset_new_pin_final
    print(new_pin_final)
    print(reset_new_pin_final)

    if(new_pin_final== reset_new_pin_final):
        updated_pin= ("UPDATE card_details SET pin=%i  WHERE Acc_No=%i" % (int(reset_new_pin_final),int(acc_entry.get())))
        mycursor.execute(updated_pin)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        messagebox.showinfo("PIN changed", "PIN reset successfully")

    else:
        messagebox.showerror("PIN changed", "Unable to reset PIN...make sure you re-enter the same PIN again")
        openDashboard()



                

   
    
######################################################################################################################################
def openfingscan():
    return true

def openfacescan():
    return true




####################################################################################################################################

                                                                                                                            ###AUTHENTICATION PAGE CODE#######

def openAuthentication():
    root3 = Toplevel()
    root3.title("AUTHENTICATION")
    root3.geometry('1920x1080')



    #Frame1 and its details
    frame1 = tk.LabelFrame(root3,bg="white", highlightbackground="white", highlightthickness="3")
    frame1.place(x=0, y=0, width=1280, height=120)

    logo3= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
    logo3ref=logo3
    label=ttk.Label(frame1, image=logo3ref)
    label.image=logo3ref
    label.place(x=-30, y=-30, width=60, height=60)


    head1=Label(frame1, text="QUERENCIA", bg="white", fg="black", font=("times new roman", 25, "bold"))
    head1.place(x=40, y=30)
    head2=Label(frame1, text="Toll free: 0900-0723-0213", bg="white", fg="black", font=("times new roman", 10))
    head2.place(x=45, y=70)


    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #Frame2 and its details

    frame2 = tk.LabelFrame(root3,bg="black", highlightbackground="white", highlightthickness="3" )
    frame2.place(x=0, y=120, width=640, height=1160)
    

    # Load the image
    image1=Image.open('D:/College/BE project/proj final/Images/fingerprint.png')

    # Resize the image in the given (width, height)
    img1=image1.resize((100, 100))

    # Conver the image in TkImage
    my_img1=ImageTk.PhotoImage(img1)
    img1ref=my_img1

    # Display the image with label
    label=Label(frame2, image=img1ref)
    label.image=img1ref
    label.pack()
    label.place(x=275, y=120)

    fingerprint= Label(frame2, text="Select an image for fingerprint verification", fg="#00B9FF", bg="black", font=("calibri", 14, "bold"))
    fingerprint.place(x=160, y=280)


    fing=tk.Button(frame2, text="Proceed", font=('Helvetica','15'), command=openfingscan)
    fing.place(x=285, y=370, width=85, height=40)
    fing.configure(bg="white", fg="#242728")

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #Frame3 and its details

    frame3 = tk.LabelFrame(root3,bg="#797D7F", highlightbackground="white", highlightthickness="3")
    frame3.place(x=640, y=120, width=640, height=1160)

    # Load the image
    image2=Image.open('D:/College/BE project/proj final/Images/face.png')

    # Resize the image in the given (width, height)
    img2=image2.resize((100, 100))

    # Conver the image in TkImage
    my_img2=ImageTk.PhotoImage(img2)
    img2ref=my_img2

    # Display the image with label
    label=Label(frame3, image=img2ref)
    label.image=img2ref
    label.pack()
    label.place(x=275, y=120)

    face= Label(frame3, text="Use face scanner to capture your face", fg="#00B9FF", bg="#7B7D7D", font=("calibri", 14, "bold"))
    face.place(x=175, y=280)

    face=tk.Button(frame3, text="Proceed", font=('Helvetica','15'), state="disabled", command=openfacescan)
    face.place(x=285, y=370, width=85, height=40)
    face.configure(bg="white", fg="#242728")

    cont=tk.Button(frame3, text="Continue", state="disabled", font=('Helvetica','20'))
    cont.place(x=490, y=450, width=135, height=40)
    cont.configure(bg="black", fg="#00B9FF")

##################################################################################################################################

def openDashboard():
    global a

    a=acc_entry.get()
    p=pswd_entry.get()
    key, value= a,p

    
    if (key in final and value==final[key]):
        
        root2 = Toplevel(root)
        root2.title("DASHBOARD")
        root2.geometry('1920x1080')


        #Frame1 and its details
        frame3 = tk.LabelFrame(root2,bg="white", highlightbackground="black", highlightthickness="2")
        frame3.place(x=0, y=0, width=1280, height=120)

        logo2= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
        logo2ref=logo2
        label=ttk.Label(frame3, image=logo2ref)
        label.image=logo2ref
        label.place(x=-30, y=-30, width=60, height=60)

        title1=Label(frame3, text="QUERENCIA", bg="white", fg="black", font=("times new roman", 25, "bold")).place(x=40, y=30)
        title2=Label(frame3, text="Toll free: 0900-0723-0213", bg="white", fg="black", font=("times new roman", 10)).place(x=45, y=70)

        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        #Display time in real-time.....check later...not working right now  (only static time is getting displayed)....error in after() method

        IST=pytz.timezone('Asia/Kolkata')

        def update_clock():
            raw_TS=datetime.now(IST)
            date_now=raw_TS.strftime("%d %b %Y")
            time_now=raw_TS.strftime("%H: %M: %S %p")
            label1=Label(frame1, text=date_now, bg="white", fg="black", font=("times new roman", 15, "bold")).place(x=1130, y=30)
            label2=Label(frame1, text=time_now, bg="white", fg="black", font=("times new roman", 15, "bold")).place(x=1130, y=60)
            #label2.after(1000, update_clock)
            
        #update_clock()
        #now = datetime.datetime.now()
        #print (now.strftime("%Y-%m-%d %H:%M:%S"))
        # Create Label to display the Date
        #label = Label(frame1, text=now.strftime("%Y-%m-%d %H:%M:%S"), font="Calibri, 10").place(x=200, y=70)

        #root.after(0, update_clock)

        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        #Frame2 and its details

        frame4 = tk.LabelFrame(root2,bg="#242728", highlightbackground='white', highlightthickness="3")
        frame4.place(x=0, y=120, width=1280, height=1120)

        title=Label(frame4, text="Please select your desired transaction:", bg="#242728", fg="#00B9FF", font=("times new roman", 25, "bold")).place(x=360, y=60)

        # Load the image
        image1=Image.open('D:/College/BE project/proj final/Images/withdraw.png')

        # Resize the image in the given (width, height)
        img1=image1.resize((90, 90))

        # Conver the image in TkImage
        my_img1=ImageTk.PhotoImage(img1)

        img1ref=my_img1

        # Display the image with label
        label=Label(frame4, image=img1ref)
        label.image=img1ref
        label.pack()
        label.place(x=200, y=180)

        w=tk.Button(frame4, text="WITHDRAW", font=('calibri','14', 'bold'), command=openWithdraw)
        w.place(x=188, y=290, width=120, height=40)
        w.configure(bg="black", fg="#00B9FF")


        # Load the image
        image2=Image.open('D:/College/BE project/proj final/Images/deposit.png')

        # Resize the image in the given (width, height)
        img2=image2.resize((90, 90))

        # Conver the image in TkImage
        my_img2=ImageTk.PhotoImage(img2)

        img2ref=my_img2

        # Display the image with label
        label=Label(frame4, image=img2ref)
        label.image=img2ref
        label.pack()
        label.place(x=450, y=180)

        d=tk.Button(frame4, text="DEPOSIT", font=('calibri','14', 'bold'), command=openDeposit)
        d.place(x=448, y=290, width=100, height=40)
        d.configure(bg="black", fg="#00B9FF")




        # Load the image
        image3=Image.open('D:/College/BE project/proj final/Images/balance.png')

        # Resize the image in the given (width, height)
        img3=image3.resize((90, 90))

        # Conver the image in TkImage
        my_img3=ImageTk.PhotoImage(img3)
        img3ref=my_img3

        # Display the image with label
        label=Label(frame4, image=img3ref)
        label.image=img3ref
        label.pack()
        label.place(x=700, y=180)


        b=tk.Button(frame4, text="BALANCE  ENQUIRY", font=('calibri','14', 'bold'), command=viewBalance)
        b.place(x=660, y=290, width=180, height=40)
        b.configure(bg="black", fg="#00B9FF")




        # Load the image
        image4=Image.open('D:/College/BE project/proj final/Images/lock.png')

        # Resize the image in the given (width, height)
        img4=image4.resize((90, 90))

        # Conver the image in TkImage
        my_img4=ImageTk.PhotoImage(img4)
        img4ref=my_img4

        # Display the image with label
        label=Label(frame4, image=img4ref)
        label.image=img4ref
        label.pack()
        label.place(x=950, y=180)


        b=tk.Button(frame4, text="CHANGE PIN", font=('calibri','14', 'bold'), command=pinChange)
        b.place(x=934, y=290, width=128, height=40)
        b.configure(bg="black", fg="#00B9FF")

        

        #button

       # db2=tk.Button(frame4, text="Continue", font=('Helvetica','20'), )
        #db2.place(x=1110, y=450, width=135, height=50)
        #db2.configure(bg="white", fg="#242728")

    else:
        messagebox.showerror("LOGIN UNSUCCESSFUL", "INVALID ACCOUNT NUMBER OR PIN...PLEASE TRY AGAIN.")


#################################################################################################################################################

def openRefresh():
    root.withdraw()
    os.system("python linked_home_dash_auth_version3.py")



    
    

##############################HOME PAGE CODE STARTS BELOW#######################

#DATABASE CONNECTIVITY#
    
def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='test',
                                       user='root',
                                       #password='Mysql@41*',
                                       port='3307')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#HOME WINDOW


root = Tk()
root.title("QUERENCIA")
root.geometry('1920x1080')


def openHelp():
    helpwindow = Toplevel()
    helpwindow.title("HELP")
    helpwindow.geometry('1920x1080')

    #Frame1 and its details
    frame1 = tk.LabelFrame(helpwindow,bg="black",highlightbackground="white", highlightthickness="3")
    frame1.place(x=0, y=0, width=1280, height=250)

    frame2 = tk.LabelFrame(helpwindow,bg="black",highlightbackground="white", highlightthickness="3")
    frame2.place(x=0, y=250, width=1280, height=830)

    logo= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
    logoreference=logo
    label=ttk.Label(frame1, image=logoreference)
    label.image=logoreference
    label.place(x=-30, y=-30, width=60, height=60)

    title=Label(frame1, text="Welcome to Querencia!", bg="black", fg="white", font=("times new roman", 35, "bold")).place(x=360, y=30)
    title2=Label(frame1, text="Customer first, everything later!", bg="black", fg="#00B9FF", font=("Verdana", 13, "bold")).place(x=450, y=100)
    title3=Label(frame1, text="Toll free: 0900-0723-0213", bg="black", fg="#e3e8e8", font=("times new roman", 10, "bold")).place(x=533, y=170)
    
    title4=Label(frame2, text="HOW TO USE THE SYSTEM?", bg="black", fg="orange", font=("times new roman", 20)).place(x=420, y=10)
    title5=Label(frame2, text="1. Enter your 9-digit account number and 4-digit PIN and click on continue.", bg="black", fg="white", font=("calibri", 15)).place(x=20, y=80)
    title6=Label(frame2, text="2. Select your desired transaction from the dashboard.", bg="black", fg="#00B9FF", font=("calibri", 15)).place(x=20, y=110)
    title7=Label(frame2, text="3. For 'Withdraw' and 'Deposit' transactions, enter the amount and click on proceed.", bg="black", fg="white", font=("calibri", 15)).place(x=20, y=140)
    title8=Label(frame2, text="4. For 'PIN change', enter the new PIN, then re-enter the new PIN and click on reset pin.", bg="black", fg="#00B9FF", font=("calibri", 15)).place(x=20, y=170)
    title9=Label(frame2, text="5. Verify your biometric details and click on proceed.", bg="black", fg="white", font=("calibri", 15)).place(x=20, y=200)
    title10=Label(frame2, text="6. Wait for your transaction to complete. In case of any error, you will be notified about the same. Kindly retry your transaction.", bg="black", fg="#00B9FF", font=("calibri", 15)).place(x=20, y=230)
    title11=Label(frame2, text="7. Do not forget to take your ATM card back once your transaction has been done.", bg="black", fg="white", font=("calibri", 15)).place(x=20, y=260)
    title12=Label(frame2, text="8. If any problem still persists, feel free to contact us. Querencia is always available for the customers!", bg="black", fg="#00B9FF", font=("calibri", 15)).place(x=20, y=290)
    title13=Label(frame2, text="9. Rest assured at any time that all your details are completely safe in our system database.", bg="black", fg="white", font=("calibri", 15)).place(x=20, y=320)

    helpwindow.mainloop()




#Frame1 and its details
frame1 = tk.LabelFrame(root,bg="#242728", highlightbackground="white", highlightthickness="3")
frame1.place(x=0, y=0, width=900, height=700)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Display time in real-time.....check later...not working right now  (only static time is getting displayed)....error in after() method

IST=pytz.timezone('Asia/Kolkata')

def update_clock():
    raw_TS=datetime.now(IST)
    date_now=raw_TS.strftime("%d %b %Y")
    time_now=raw_TS.strftime("%H: %M: %S %p")
    label1=Label(frame1, text=date_now, bg="#242728", fg="white", font=("times new roman", 15, "bold")).place(x=500, y=30)
    label2=Label(frame1, text=time_now, bg="#242728", fg="white", font=("times new roman", 15, "bold")).place(x=100, y=30)
  #  label2.after(1000, update_clock)
    
#update_clock()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


title=Label(frame1, text="Welcome to Querencia!", bg="#242728", fg="white", font=("times new roman", 45, "bold")).place(x=150, y=100)
title2=Label(frame1, text="Customer first, everything later!", bg="#242728", fg="#00B9FF", font=("Verdana", 20, "bold")).place(x=200, y=180)
title3=Label(frame1, text="Toll free: 0900-0723-0213", bg="#242728", fg="orange", font=("times new roman", 15, "bold")).place(x=330, y=350)

logo1= tk.PhotoImage(file="D:/College/BE project/proj final/Images/logo.png")
label=ttk.Label(frame1, image=logo1)
label.place(x=-30, y=-30, width=60, height=60)

helpbutton=tk.Button(frame1, text="Help", font=('Helvetica','20'), command=openHelp)
helpbutton.place(x=100, y=590, width=80, height=40)
helpbutton.configure(bg="white", fg="#00B9FF")

refreshbutton=tk.Button(frame1, text="Refresh", font=('Helvetica','20'), command=openRefresh)
refreshbutton.place(x=670, y=590, width=120, height=40)
refreshbutton.configure(bg="white", fg="#00B9FF")


    
#frame2 and its details
frameh = tk.LabelFrame(root,bg="#00B9FF", highlightbackground="black", highlightthickness="3")
frameh.place(x=900, y=0, width=480, height=700)

acc_label= Label(frameh, text="ENTER ACCOUNT NO:", fg="black", bg="#00B9FF", font=("times new roman", 20, "bold")).place(x=40, y=20)
acc_entry= Entry(frameh, width=30, font=("calibri", 15, "bold"), textvariable="bal")
acc_entry.place(x=40, y=60)

pswd_label= Label(frameh, text="ENTER YOUR PIN:", fg="black", bg="#00B9FF", font=("times new roman", 20, "bold")).place(x=40, y=150)
pswd_entry= Entry(frameh, width=30, font=("calibri", 15, "bold"), show="*")
#pswd_entry.config(state= "disabled")
pswd_entry.place(x=40, y=190)


    
count=0
countp=0
char_acc=0
char_pin=0

def on_click(text):

    global count
    global countp
    global char_acc
    global char_pin


    if(text=="00" and count>=8):
        return 0
        
    elif(text=="00" and count<=7):
        count=count+2
        #char_acc=char_acc+2
        acc_entry.insert("end", text)
        if(count>=9):
             acc_entry.config(state="disabled")

    elif(count<=8):
        count=count+1
        #char_acc=char_acc+1
        acc_entry.insert("end", text)
        if(count>=9):
            acc_entry.config(state="disabled")
            #doublezero.configure(state="normal")
    
    else:
        
        if(text=="00" and countp<=2):
            countp=countp+2
            #char_pin=char_pin+2
            pswd_entry.insert("end", text)
            if(countp>=4):
                pswd_entry.config(state="disabled")
                home_cont.config(state="normal")
                

        elif(countp<4):
            countp=countp+1
            #char_pin=char_pin+1
            pswd_entry.insert("end", text)
            if(countp>=4):
                pswd_entry.config(state="disabled")
                home_cont.config(state="normal")
            
        else:
            pswd_entry.config(state="disabled")
            

def clear():
    global count
    global countp
    #global char_acc
    #global char_pin
    
    if(char_pin==0 and char_acc!=9):
        acc_entry.delete(count-1, "end")
        #char_acc=char_acc-1
        count=count-1

    else:
        pswd_entry.delete(count-1, "end")
        #char_pin=char_pin-1
        countp=countp-1
  

                

one=tk.Button(frameh, text="1", font=('Helvetica','30', "bold"), command=lambda:on_click("1"))
one.place(x=90, y=300, width=40, height=40)
one.configure(bg="white", fg="#242728")
    
two=tk.Button(frameh, text="2", font=('Helvetica','30', "bold"), command=lambda:on_click("2"))
two.place(x=170, y=300, width=40, height=40)
two.configure(bg="white", fg="#242728")

three=tk.Button(frameh, text="3", font=('Helvetica','30', "bold"), command=lambda:on_click("3"))
three.place(x=250, y=300, width=40, height=40)
three.configure(bg="white", fg="#242728")

four=tk.Button(frameh, text="4", font=('Helvetica','30', "bold"), command=lambda:on_click("4"))
four.place(x=90, y=370, width=40, height=40)
four.configure(bg="white", fg="#242728")

five=tk.Button(frameh, text="5", font=('Helvetica','30', "bold"), command=lambda:on_click("5"))
five.place(x=170, y=370, width=40, height=40)
five.configure(bg="white", fg="#242728")

six=tk.Button(frameh, text="6", font=('Helvetica','30', "bold"), command=lambda:on_click("6"))
six.place(x=250, y=370, width=40, height=40)
six.configure(bg="white", fg="#242728")

seven=tk.Button(frameh, text="7", font=('Helvetica','30', "bold"), command=lambda:on_click("7"))
seven.place(x=90, y=440, width=40, height=40)
seven.configure(bg="white", fg="#242728")

eight=tk.Button(frameh, text="8", font=('Helvetica','30', "bold"), command=lambda:on_click("8"))
eight.place(x=170, y=440, width=40, height=40)
eight.configure(bg="white", fg="#242728")

nine=tk.Button(frameh, text="9", font=('Helvetica','30', "bold"), command=lambda:on_click("9"))
nine.place(x=250, y=440, width=40, height=40)
nine.configure(bg="white", fg="#242728")

doublezero=tk.Button(frameh, text="00", font=('Helvetica','25', "bold"), command=lambda:on_click("00"))
doublezero.place(x=90, y=510, width=40, height=40)
doublezero.configure(bg="white", fg="#242728")

zero=tk.Button(frameh, text="0", font=('Helvetica','30', "bold"), command=lambda:on_click("0"))
zero.place(x=170, y=510, width=40, height=40)
zero.configure(bg="white", fg="#242728")

# Load the image
cross1=Image.open('D:/College/BE project/proj final/Images/cross.png')

# Resize the image in the given (width, height)
cro1=cross1.resize((35, 35))

# Conver the image in TkImage
my_cross1=ImageTk.PhotoImage(cro1)

# Display the image with label
label=Label(frameh, image=my_cross1)
label.pack()
label.place(x=250, y=510)

back=tk.Button(frameh, image=my_cross1, font=('Helvetica','30', "bold"), command=clear)
back.place(x=250, y=510, width=40, height=40)
back.configure(bg="white", fg="#242728")


home_cont=tk.Button(frameh, text="Continue", font=('Helvetica','20'), state="disabled", command= openDashboard)
home_cont.place(x=125, y=590, width=130, height=40)
home_cont.configure(bg="#242728", fg="white")


mydb = mysql.connector.connect(host='localhost', database='test',user='root', port='3307')
mycursor= mydb.cursor()

login_credentials="SELECT Acc_No, pin FROM card_details"
mycursor.execute(login_credentials)

result= mycursor.fetchall()

for row in result:
    print(row)

final=(dict(result))
print(final)
print("\n")


    
#################################################################################################################################################

root.mainloop()
