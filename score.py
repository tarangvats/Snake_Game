ALIGNMENT = "center"
FONT = ("Courier",24, "normal")
from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0,250)
    def update(self):
        self.sc = self.sc + 1
    def print(self):
        self.write(f"Score: {self.sc}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
