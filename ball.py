from turtle import Turtle
FORWARD_BOUNCE = 10
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = random.randint(1, 11)
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset_ball(self):
        self.move_speed = 0.1
        self.goto(x=0, y=0)
        self.ball_bounce_x()

