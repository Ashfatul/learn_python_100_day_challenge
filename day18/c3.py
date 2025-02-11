from turtle import Turtle, Screen
import random

tom = Turtle()
tom.shape("turtle")
tom.shapesize(2, 2, 10)
tom.speed(10)
colors = [
    "red", "blue", "green", "yellow", "purple", 
    "orange", "pink", "brown", "black", "white", 
    "gray", "cyan", "magenta", "lime", "maroon", 
    "navy", "olive", "teal", "gold", "violet"
]


def drawshape(number_of_sides):
    count = 3

    def draw(sides):
        for _ in range(sides):
            tom.forward(150)
            tom.left(360 / sides)

    while count <= number_of_sides:
        tom.color(random.choice(colors))
        draw(count)
        count += 1

drawshape(20)

screen = Screen()
screen.exitonclick()
