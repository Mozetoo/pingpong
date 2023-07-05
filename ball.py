from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ballcontrolx = 10
        self.ballcontroly = 10
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        x_c = self.xcor() + 2 + self.ballcontrolx
        y_c = self.ycor() + 2 + self.ballcontroly
        self.goto(x_c, y_c)

    def changex(self):
        self.ballcontrolx *= -1

    def changey(self):
        self.ballcontroly *= -1

    def miss(self):
        self.goto(0, 0)
        self.changex()
