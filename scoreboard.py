from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-180, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(180, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 50, "normal"))

    def update_l_score(self):
        self.clear()
        self.l_score += 1
        self.write_score()

    def update_r_score(self):
        self.clear()
        self.r_score += 1
        self.write_score()