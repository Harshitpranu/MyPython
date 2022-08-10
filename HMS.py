from tkinter import *
from tkinter import messagebox

import pymysql

taz=Tk()
########################################## Main Heading ##########################################
def mainheading():
    label=Label(taz,text="Hotel Management System",bg="light blue",fg="red",font=('comic sans ms',48,"bold"),padx=165)
    label.grid(row=0,columnspan=5)
################################# Data Dase connection  #############################################
def dbconnect():
    global connection,mycursor
    connection=pymysql.Connect(user="root",host="127.0.0.1",db='pranu_hotel')
    mycursor=connection.cursor()
######################################## Remove Window ###########################################
def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

def ItemWindow():
    remove_all_widgets()
    mainheading()
    itemnameLabel = Label(taz, text="ITEM DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=2, padx=(50, 0), columnspan=1, pady=10)
################################## All Functions #############################################
def all_function():
    management = Button(taz, text='Management', font=('comic sans ms', 15, "bold"),command=ItemWindow)
    management.grid(row=1, column=0, padx=200)
    billing = Button(taz, text='Billing', font=('comic sans ms', 15, "bold"))
    billing.grid(row=1, column=1, padx=200)
    receipt = Button(taz, text='Receipt', font=('comic sans ms', 15, "bold"))
    receipt.grid(row=2, column=0, columnspan=2, padx=200)
####################################### welcome window ######################################
def welcomewindow():
    remove_all_widgets()
    mainheading()
    all_function()


###################################### admin login ##############################################
usernameVar=StringVar()
passwordVar=StringVar()
def adminlogin():
    username=usernameVar.get()
    password=passwordVar.get()
    if username=="" or password=="":
        messagebox.showerror("login Error","Please Enter Both Fields")
    else:
        dbconnect()
        que="select * from login_info where binary username=%s and binary password=%s"
        val=(username,password)
        mycursor.execute(que,val)
        data=mycursor.fetchall()
        flag=False
        for row in data:
            flag=True
        connection.close()
        if flag==True:
            welcomewindow()
            print("connected")
        else:
            messagebox.showerror('Invalid user Credential',"Either Username or Password wrong")
            usernameVar.set("")
            passwordVar.set("")
#################################### Login Window ############################################
def loginwindow():
    loginlabel=Label(taz,text="Admin login",font=("arial",30,"bold","italic"),fg='black')
    loginlabel.grid(row=1,column=1,padx=(50.0),columnspan=2,pady=10)
    username=Label(taz,text="Username",font=("arial 10"),padx=20,pady=5)
    username.grid(row=2,column=1)
    password=Label(taz,text="Password",font=("arial 10"))
    password.grid(row=3,column=1,padx=20,pady=5)
    usernameEntry=Entry(taz,textvariable=usernameVar,bd=5)
    usernameEntry.grid(row=2,column=2,padx=20,pady=5)
    PasswordEntry =Entry(taz,textvariable=passwordVar,bd=5)
    PasswordEntry.grid(row=3, column=2, padx=20, pady=5)
    loginbutton=Button(taz,text="Login",width=20,height=2,command=adminlogin,bd=5)
    loginbutton.grid(row=4,column=1,columnspan=2)
loginwindow()
mainheading()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()