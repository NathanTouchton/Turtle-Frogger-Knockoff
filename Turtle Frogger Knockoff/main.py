from turtle import Screen
from time import sleep
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

car = CarManager()

scoreboard = Scoreboard()

screen.onkeypress(fun=player.move, key="Up")

GAME_IS_ON = True
CAR_VARIABLE = 5
while GAME_IS_ON:
    sleep(0.1)
    screen.update()
    CAR_VARIABLE -= 1
    if CAR_VARIABLE == 0:
        car.create_car()
        CAR_VARIABLE = 5

    car.move()

    for item in car.car_list:
        if item.distance(player) <= 20:
            scoreboard.game_over()
            GAME_IS_ON = False

    if player.ycor() >= 250:
        player.goto(STARTING_POSITION)
        car.move_increment += 3
        scoreboard.increase_score()
        scoreboard.print_score()

screen.exitonclick()

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
# No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
# Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.

# Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.

# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
# When this happens, return the turtle to the starting position and increase the speed of the cars. 
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing,the level should increase.
# When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
