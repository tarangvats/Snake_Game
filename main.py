from snake import Snake
from turtle import Turtle,Screen
import time



s = Screen()
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

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    sn.snake_move()
    x = sn.segments[2].xcor()
    y = sn.segments[2].ycor()
    if x >= 290 or x <= -290 or y >= 290 or y <= -290:
        game_is_on = False
        print("You Lost")


s.exitonclick()
