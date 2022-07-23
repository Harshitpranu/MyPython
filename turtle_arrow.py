from turtle import *
t1=Turtle()
t2=Turtle()
t1.pencolor('blue')
t2.pencolor('red')
t1.penup()
t2.penup()
t1.goto(-200,0)
t2.goto(200,0)
t2.lt(180)
t1.pendown()
t2.pendown()
for i in range(1,11):
    t2.fd(35)
    t2.penup()
    t2.fd(5)
    t2.pendown()
for e in range(3):
    for i in range(1,11):
        t2.undo()
        t2.undo()
        t2.undo()
        t2.undo()
        t1.fd(35)
        t1.penup()
        t1.fd(5)
        t1.pendown()
    for i in range(1,11):
        t1.undo()
        t1.undo()
        t1.undo()
        t1.undo()
        t2.fd(35)
        t2.penup()
        t2.fd(5)
        t2.pendown()


done()