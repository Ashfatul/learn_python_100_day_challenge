from turtle import Screen
from ball import Ball
from paddle import Paddle

window = Screen()
window.setup(height=600, width=800)
window.bgcolor("black")
window.title("Pong")
window.listen()

ball = Ball()

paddle1 = Paddle()
paddle1_head = paddle1.getHeadPosition()

paddle2 = Paddle()
paddle2_head = paddle1.getHeadPosition()

window.onkey(paddle1.move_up, "w")
window.onkey(paddle1.move_down, "s")













window.exitonclick()