from turtle import *
from ball import *
from paddle import *
from scoreboard import *
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")

keepon = True
ball = Ball()
screen.tracer(0)
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
score = Scores()
screen.tracer(1)
ball.speed(0)
screen.listen()
screen.onkey(fun=paddle_l.upp, key="Up")
screen.onkey(paddle_l.downn, "Down")
screen.onkey(fun=paddle_r.upp, key="w")
screen.onkey(paddle_r.downn, "s")
delay = 0.1

while keepon:
    time.sleep(delay)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.changey()
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320 or ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.changex()
        delay *=0.9
    if ball.xcor() < -380:
        ball.miss()
        score.r_point()
        delay = 0.1
    if ball.xcor() > 380:
        ball.miss()
        score.l_point()
        delay = 0.1

screen.exitonclick()
