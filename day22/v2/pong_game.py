from turtle import Turtle, Screen

window = Screen()
window.setup(1600, 1000)
window.bgcolor("black")
starter = Turtle()
starter.penup()
starter.hideturtle()
starter.teleport(0, 0)
starter.color("white")
starter.write("Press S to start", align="center", font=("Arial", 25, "normal"))
window.listen()
window.exitonclick()
