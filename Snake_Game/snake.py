from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)


    def move(self):
        for snake_num in range(len(self.parts) - 1, 0, -1):
            x_cord = self.parts[snake_num - 1].xcor()
            y_cord = self.parts[snake_num - 1].ycor()

            self.parts[snake_num].goto(x_cord, y_cord)

        self.head.forward(MOVE_DISTANCE)

    def add_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.parts.append(new_part)
        print(new_part.position())

    def extend(self):
        self.add_part(self.parts[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
