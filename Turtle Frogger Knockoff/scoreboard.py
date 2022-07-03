from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(x=0, y=260)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Level {self.level_number}", align="center", font=(FONT))

    def increase_score(self):
        self.level_number += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align="center", font=(FONT))

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing,the level should increase.
# When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
