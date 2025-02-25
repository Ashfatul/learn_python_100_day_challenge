from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,350)
        self.write(f"Your Score = {self.score}", align="center", font=("Arial", 10, "bold"))
        
    def updateScore(self):
        self.clear()
        self.score += 1
        self.write(f"Your Score = {self.score}", align="center", font=("Arial", 10, "bold"))
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Arial", 20, "bold"))