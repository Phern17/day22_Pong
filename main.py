import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong by Python")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # detect collision with the wall and bounce
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.ball_bounce_y()

    # detect collision with the paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.ball_bounce_x()

    # detect if player misses the ball
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.update_l_score()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.update_r_score()


screen.exitonclick()
