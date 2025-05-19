from turtle import Turtle, Screen
from player import Player
from car import Car

window = Screen()
window.setup(1200,1200)
finish_line = Turtle()
finish_line.hideturtle()
finish_line.teleport(-500, 500)
finish_line.goto(500,500)

player = Player()

car = Car()
car2 = Car()
car3 = Car()

window.listen()
window.onkey(player.moveForword, "w")
window.onkey(player.moveBackword, "s")

window.exitonclick()