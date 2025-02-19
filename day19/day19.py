import random
from turtle import Turtle, Screen

turtles = []
turtle_colors = ["red", "green", "blue", "yellow", "orange"]
turtle_position = [300, 150, 0, -150, -300]

view = Screen()
view.setup(1000,1000)

for item in range(0,5):
    color = turtle_colors[item]
    pos = turtle_position[item]
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(color)
    turtle.shapesize(2, 2, 1)
    turtle.setx(-480)
    turtle.sety(pos)
    turtles.append(turtle)
    
    
user_input = view.textinput("Which color turtle will win the race?", "red/green/blue/yellow/orange").lower()

racing = False
winner = "Test"

if user_input != "":
    racing = True
    while racing:
        for t in turtles:
            t.forward(random.randint(0,10))
            position = t.pos()
            if position[0] > 480:
                racing = False
                winner = t.pencolor()
                
                
print(f"The winner is {winner} color")

if user_input == winner:
    print("You are a winner!\nCongratulations!!")
else:
    print(f"You are a looser! you picked ---- {user_input}\nBetter luck next time!")

    
    