from turtle import Turtle

class Paddel(Turtle):
    def __init__(self,xcord,ycord):
        super().__init__()
        self.xcord = xcord
        self.ycord = ycord
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(self.xcord, self.ycord)
        self.shapesize(stretch_wid=1, stretch_len=7)


    def go_left(self):
        cor = self.xcor()
        new_x_cor = cor - 20
        self.goto( new_x_cor, self.ycor())

    def go_right(self):
        cor = self.xcor()
        new_x_cor = cor + 20
        self.goto(new_x_cor, self.ycor())