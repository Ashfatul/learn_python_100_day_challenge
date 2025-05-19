from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self, shape = "square", visible = True):
        super().__init__(shape, visible)
        self.carColor = ["red", "green", "blue", "yellow"]
        self.turtlesize(2,5,2)
        self.color(random.choice(self.carColor))