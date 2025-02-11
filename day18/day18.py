# Draw square using turtle module

from turtle import Turtle, Screen
tom = Turtle()
tom.shape("turtle")
tom.shapesize(2,2,10)

for _ in range(0,4):
    tom.forward(100)
    tom.left(90)

screen = Screen()
screen.exitonclick()
