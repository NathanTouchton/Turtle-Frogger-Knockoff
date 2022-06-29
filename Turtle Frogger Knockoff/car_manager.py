from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.penup()
        self.seth(180)
        self.goto(x=320, y=randint(-250, 250))
        self.forward(10)

    def create_hitbox(self):
        x_coordinates = self.xcor()
        y_coordinates = self.ycor()
        right_side = x_coordinates + 20
        left_side = x_coordinates - 20
        top = y_coordinates + 20
        bottom = y_coordinates - 20

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
# No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
# Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.


# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
# When this happens, return the turtle to the starting position and increase the speed of the cars. 
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.
