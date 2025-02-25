from turtle import Turtle

class Snake:
    
    def __init__(self): 
        self.snakes = []
        self.position = [(0,0), (-20,0), (-40,0)]
        self.create_snake()
        
    def create_snake(self):
        for pos in self.position:
            self.grow(pos)
            
    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            newx = self.snakes[snake - 1].xcor()
            newy = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(newx, newy)
        
        self.snakes[0].forward(20)
        
    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)
        
    def getHead(self):
        return self.snakes[0]

    def grow(self, pos):
        snake_body = Turtle("square")
        snake_body.penup()
        snake_body.color("white")
        snake_body.goto(pos)
        self.snakes.append(snake_body)

    def increase(self):
        self.grow(self.snakes[-1].position())
