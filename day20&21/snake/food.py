from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        randomX = random.randint(-480,480)
        randomY = random.randint(-480, 480)
        self.goto(randomX, randomY)
        self.refresh()
        
    def refresh(self):
        randomX = random.randint(-480,480)
        randomY = random.randint(-480, 480)
        self.goto(randomX, randomY)