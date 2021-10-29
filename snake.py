MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create()
    def create(self):
        k = 0
        for i in range(0, 3):
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(x=k, y=0)
            k = k + 20
            self.segments.append(t)
    def snake_move(self):
        for i in range(0, len(self.segments) - 1):
            xcord = self.segments[i + 1].xcor()
            ycord = self.segments[i + 1].ycor()
            self.segments[i].goto(xcord, ycord)
        self.segments[len(self.segments) - 1].forward(MOVE_DISTANCE)

    def move_right(self):
        if self.segments[len(self.segments) - 1].heading()!=LEFT:
            self.segments[len(self.segments) - 1].setheading(RIGHT)
    def down(self):
        if self.segments[len(self.segments) - 1].heading() != UP:
            self.segments[len(self.segments) - 1].setheading(DOWN)
    def up(self):
        if self.segments[len(self.segments) - 1].heading() != DOWN:
            self.segments[len(self.segments) - 1].setheading(UP)
    def move_left(self):
        if self.segments[len(self.segments) - 1].heading() != RIGHT:
            self.segments[len(self.segments) - 1].setheading(LEFT)

    def increase_size(self):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        xc=self.segments[len(self.segments) - 1].xcor()
        yc=self.segments[len(self.segments) - 1].ycor()
        if self.segments[len(self.segments) - 1].heading() == RIGHT:
            t.goto(x=xc+20, y=yc)
        if self.segments[len(self.segments) - 1].heading() == LEFT:
            t.goto(x=xc-20, y=yc)
        if self.segments[len(self.segments) - 1].heading() == UP:
            t.goto(x=xc, y=yc+20)
        if self.segments[len(self.segments) - 1].heading() == DOWN:
            t.goto(x=xc, y=yc-20)
        t.setheading(self.segments[len(self.segments) - 1].heading())
        self.segments.append(t)
