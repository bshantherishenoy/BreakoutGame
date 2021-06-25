from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 50


class Block():
    def __init__(self):
        self.pos = -280
        self.segments=[]
        self.j = 0
        self.ypos = 230
        while self.j < 3:
            self.ypos = self.ypos - 30
            for i in range(20):
                square = Turtle("square")
                square.penup()
                square.color(random.choice(COLORS))
                square.goto(self.pos, self.ypos)
                self.pos = self.pos+30
                self.segments.append(square)
            self.j = self.j + 1
            self.pos = -280




