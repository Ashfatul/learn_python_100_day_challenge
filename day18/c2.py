# dashed line

from turtle import Turtle, Screen
tom = Turtle()
tom.shape("turtle")
tom.shapesize(2,2,10)
tom.penup()
tom.backward(500)

for _ in range(0,50):
    tom.pendown()
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = Screen()
screen.exitonclick()
