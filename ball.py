from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.xmove = 10
        self.ymove = 10

    def move(self):
        xcod = self.xcor()+self.xmove
        ycod = self.ycor()+self.ymove
        self.goto(xcod, ycod)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1


