from turtle import *


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(coordinate)

    def upp(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def downn(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
