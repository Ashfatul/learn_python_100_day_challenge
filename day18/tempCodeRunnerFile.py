from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.shapesize(2, 2, 10)

def drawshape(number_of_sides):
    count = 3  # Start with a triangle

    def draw(sides):
        for _ in range(sides):
            tom.forward(150)
            tom.left(360 / sides)

    while count <= number_of_sides:  # Loop from 3 to number_of_sides
        draw(count)
        count += 1  # Increase side count to draw the next shape

drawshape(3)

screen = Screen()
screen.exitonclick()
