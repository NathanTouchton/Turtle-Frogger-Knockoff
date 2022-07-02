from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.write(arg="test", align="center", font=(FONT))
        

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing,the level should increase.
# When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
