from turtle import Turtle

class Level(Turtle):
    def __init__(self, current_level):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.teleport(-500,520)
        self.updateLevel(current_level)
        
    def updateLevel(self, new_level):
        self.clear()
        self.write(f"Level: {new_level}", align="left", font=('Arial', 20, 'normal'))

