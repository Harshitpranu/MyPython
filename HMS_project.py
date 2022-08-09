from tkinter import *
from tkinter import messagebox
taz=Tk()

########### Main Heading #############
def mainheading():
    label=Label(taz,text="Hotel Management System",bg="light blue",fg="red",font=('comic sans ms',48,"bold"),padx=100)
    label.grid(row=0,columnspan=5)

########### admin login ############
usernameVar=StringVar()
passwordVar=StringVar()
def adminlogin():
    username=usernameVar.get()
    password=passwordVar.get()
    if username=="" or password=="":
        messagebox.showerror("login Error","Please Enter Both Fields")
########## Login Window ############
def loginwindow():
    loginlabel=Label(taz,text="Admin login",font=("arial",30,"bold","italic"),fg='black')
    loginlabel.grid(row=1,column=1,padx=(50.0),columnspan=2,pady=10)
    username=Label(taz,text="Username",font=("arial 10"),padx=20,pady=5)
    username.grid(row=2,column=1)
    password=Label(taz,text="Password",font=("arial 10"))
    password.grid(row=3,column=1,padx=20,pady=5)
    usernameEntry=Entry(taz)
    usernameEntry.grid(row=2,column=2,padx=20,pady=5)
    PasswordEntry =Entry(taz)
    PasswordEntry.grid(row=3, column=2, padx=20, pady=5)
    loginbutton=Button(taz,text="Login",width=20,height=2,command=adminlogin)
    loginbutton.grid(row=4,column=1,columnspan=2)
loginwindow()
mainheading()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()