
from tkinter import *
root=Tk()
def add():
    a=x.get()
    b=y.get()
    c=a+b
    print(c)
def sub():
    a=x.get()
    b=y.get()
    c=a-b
    print(c)
def mul():
    a=x.get()
    b=y.get()
    c=a*b
    print(c)
def div():
    a=x.get()
    b=y.get()
    c=a/b
    print(c)

x=IntVar()
y=IntVar()

label1=Label(root,text="1st number",font=("comic sans ms",15,"bold"),bg="light blue")
label1.place(x=0,y=50)
label2=Label(root,text="2nd number",font=("comic sans ms",15,"bold"),bg="light blue")
label2.place(x=0,y=100)
text1=Entry(root,font=("comic sans ms",10,"bold"),textvariable=x)
text1.place(x=150,y=55)
text2=Entry(root,font=("comic sans ms",10,"bold"),textvariable=y)
text2.place(x=150,y=105)

btn1=Button(root,text="+",font=("comic sans ms",15),command=add)
btn1.place(x=25,y=200)
btn2=Button(root,text="-",font=("comic sans ms",16),command=sub)
btn2.place(x=125,y=200)
btn3=Button(root,text="*",font=("comic sans ms",15),command=mul)
btn3.place(x=25,y=300)
btn4=Button(root,text="/",font=("comic sans ms",15),command=div)
btn4.place(x=125,y=300)

root.geometry("200x400+400+200")
root.mainloop()