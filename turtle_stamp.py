from turtle import *
t=Turtle()
t.pencolor('blue')
t.fillcolor('red')
t.shape('square')
t.shapesize(5,5,5)
t.penup()
t.goto(200,200)
t.stamp()
t.goto(-200,200)
t.stamp()
t.goto(-200,-200)
t.stamp()
t.goto(200,-200)
t.stamp()
t.home()
t.stamp()
done()
