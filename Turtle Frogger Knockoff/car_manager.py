from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.penup()
        self.seth(180)

    # def create_car(self):

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
# No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
# Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.
