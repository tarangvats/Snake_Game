MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle,Screen
import time
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
        if self.segments[2].heading()!=LEFT:
            self.segments[2].setheading(RIGHT)
    def down(self):
        if self.segments[2].heading() != UP:
            self.segments[2].setheading(DOWN)
    def up(self):
        if self.segments[2].heading() != DOWN:
            self.segments[2].setheading(UP)
    def move_left(self):
        if self.segments[2].heading() != RIGHT:
            self.segments[2].setheading(LEFT)
