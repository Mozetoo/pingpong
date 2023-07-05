from turtle import *
from paddle import *

# def setup():
#     screen.setup(800, 600)
#     screen.bgcolor("black")
#     screen.title("Pong")
#
#     tim.color("white")
#     tim.seth(90)
#     tim.penup()
#     tim.hideturtle()
#     tim.speed(0)
#     tim.pensize(width=3)
#     tim.goto(0, -300)
#
#
# p1_pos = [(350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]


# def line():
#     for _ in range(100):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))
screen.tracer(1)
screen.listen()
screen.onkey(fun=paddle_1.upp, key="Up")
screen.onkey(paddle_1.downn, "Down")
screen.onkey(fun=paddle_2.upp, key="w")
screen.onkey(paddle_2.downn, "s")

screen.exitonclick()
