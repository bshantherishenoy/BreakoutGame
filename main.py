from turtle import Turtle, Screen
from paddel import Paddel
from ball import Ball
from blocks import Block
from score import Score
import time

screen = Screen()
screen.setup(600,600)
screen.title("Breakout Game")
screen.tracer(0)
screen.bgcolor("black")

paddle_l = Paddel(0, -280)

screen.listen()

screen.onkey(paddle_l.go_left, "Left")
screen.onkey(paddle_l.go_right, "Right")

score = Score()
blocks = Block()


def play_game():
    game_is_on = True
    ball = Ball()
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball.move()
        for car in blocks.segments:
            print("car distance less true")
            print(f"the distance of car with the ball is------------------------------{ball.distance(car)}")
            if ball.distance(car) < 20:
                car.goto(1000,1000)
                score.scoreadd()

        if ball.ycor() > 280 or ball.ycor() < -280:
            print("yes")
            print(ball.xcor(), ball.ycor())
            ball.bounce_y()

        if ball.xcor() < -280 or ball.xcor() > 280:
            print("True")
            ball.bounce_x()
            ball.speed("slow")

        if ball.distance(paddle_l) < 50:
            ball.bounce_y()
            print("The ball touched the paddele")

        if ball.ycor() == -280:
            game_is_on = False
            score.gameouer()



play_game()
screen.exitonclick()