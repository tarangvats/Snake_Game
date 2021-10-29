from snake import Snake
from turtle import Turtle,Screen
from food import Food
from score import Score
import time



s = Screen()
f = Food()
score=Score()

s.setup(height=600,width=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
sn = Snake()
s.listen()
s.onkey(sn.move_left,key="Left")
s.onkey(sn.up,key="Up")
s.onkey(sn.down,key="Down")
s.onkey(sn.move_right,key = "Right")

a = f.xcor()
b = f.ycor()
sr=0
game_is_on = True
while game_is_on:

    s.update()
    time.sleep(0.1)
    sn.snake_move()
    x = sn.segments[len(sn.segments) - 1].xcor()
    y = sn.segments[len(sn.segments) - 1].ycor()
    score.clear()
    score.print()
    if x >= 290 or x <= -290 or y >= 250 or y <= -290:
        game_is_on = False
        score.game_over()
        print(f"Your score is {sr}")
    if sn.segments[len(sn.segments) - 1].distance(f) <=15:
        sr = sr +1
        f.refresh()
        score.update()
        sn.increase_size()


s.exitonclick()
