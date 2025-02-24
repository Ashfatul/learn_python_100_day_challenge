from turtle import Turtle, Screen
from snake import Snake
import time
window = Screen()
window.setup(width=1000,height=1000)
window.bgcolor("black")
window.tracer(0)

window.title("Snake Game")
window.listen()
snakes = []
position = 0
game_on = True

writer = Turtle()
writer.color("white")
writer.penup()
writer.goto(0, 400)
writer.hideturtle()
writer.write("Snake Game", align="center", font=("Arial", 16, "bold"))

snake = Snake() 
    

window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")




while game_on:
    window.update()
    time.sleep(0.1)
    snake.move()

window.exitonclick()