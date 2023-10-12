from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("साँप का खेल")
screen.tracer(0)

game = True
score = Scoreboard()
s = Snake()
food = Food()
screen.listen()
screen.onkey(key="Up", fun=s.up)
screen.onkey(key="Down", fun=s.down)
screen.onkey(key="Right", fun=s.right)
screen.onkey(key="Left", fun=s.left)
while game:
    screen.update()
    time.sleep(0.07)
    s.move()
    if s.segments[0].distance(food) < 20:
        food.relocate()
        score.update()
        s.extend(s.segments[-1].xcor(), s.segments[-1].ycor())
        print("Nom")

    if s.collision():
        #game = False
        score.reset()
        s.reset()
    if abs(s.segments[0].xcor())>290 or abs(s.segments[0].ycor())>290:
        #game = False
        score.reset()
        s.reset()

screen.exitonclick()