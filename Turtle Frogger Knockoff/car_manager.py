from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_car()
        self.move_increment = 7

    def create_car(self):
        car = Turtle()
        car.color(choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2)
        car.penup()
        car.seth(180)
        car.goto(x=320, y=randint(-250, 250))
        self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.forward(self.move_increment)

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
# No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
# Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.


# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
# When this happens, return the turtle to the starting position and increase the speed of the cars. 
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.
