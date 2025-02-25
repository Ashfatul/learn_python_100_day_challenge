# turtle explore game

from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.shapesize(3,3,1)
tom.color("red")
tom.penup()
tom.teleport(-500,500)
tom.write("Welcome to turtle explore game", font=("Monospace", 22))
tom.teleport(-450,450)
tom.write("Use W/S/A/D or Up/Down/Left/Right key to control turtle", font=("Monospace", 10))
tom.home()

view = Screen()
view.listen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)
    
def turn_left():
    tom.left(10)
    
def turn_right():
    tom.left(-10)
    
def clear():
    tom.clear()
    tom.home()
    
view.onkey(move_forward, "w")
view.onkey(move_backward, "s")
view.onkey(turn_left, "a")
view.onkey(turn_right, "d")


view.onkey(move_forward, "Up")
view.onkey(move_backward, "Down")
view.onkey(turn_left, "Left")
view.onkey(turn_right, "Right")


view.onkey(clear, "c")
    
view.exitonclick()