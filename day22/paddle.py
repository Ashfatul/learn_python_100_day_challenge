from turtle import Turtle

class Paddle:
    def __init__(self):
            self.new_turtle = Turtle()
            self.new_turtle.penup()
            self.new_turtle.shape("square")
            self.new_turtle.color("white")
            
    def getHeadPosition(self):
        return self.turtles[0]
    
    def move_up(self):
        for item in self.turtles:
            item.forward(20)
            
    def move_down(self):
        for item in self.turtles:
            item.backward(20)
        
    
    