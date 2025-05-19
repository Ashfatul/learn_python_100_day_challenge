from turtle import Turtle
from level import Level
import time

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.left(90)
        self.teleport(0, -500)
        self.showturtle()
        self.shape("turtle")
        self.turtlesize(2, 2, 2)
        self.penup()
        self.player_lavel = 0
        self.plevel = Level(self.player_lavel)
    def moveForword(self):
        if self.ycor() < 500:
            self.forward(10)
            complete = self.levelComplete()
            
            if complete:
                self.levelUp()
                self.plevel.updateLevel(self.player_lavel)
                time.sleep(2)
                self.resetPlayerPosition()
    def moveBackword(self):
        if self.ycor() > -500:
            self.backward(10)
    def levelComplete(self):
        if self.ycor() == 500:
            return True
        else:
            return False
        
    def resetPlayerPosition(self):
        self.teleport(0,-500)
        
    def playerLavel(self):
        return self.player_lavel
    
    def levelUp(self):
        self.player_lavel += 1