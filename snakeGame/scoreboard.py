from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("hscore.txt") as s:
            self.score = int(s.read())
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("hscore.txt", mode="w") as s:
                s.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard() 
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
