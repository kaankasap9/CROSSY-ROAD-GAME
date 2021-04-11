from turtle import Screen as s
from player import Player as p
from car import Car as c
from line import Line as l
from score import Score as sc
import random as r
from end import EndScreen as e
import time

# Screen Operations
screen=s()
screen.bgcolor("grey")
screen.setup(height=800,width=1000)
screen.listen()
screen.tracer(0)

# Add Car Shapes
screen.addshape("car_blue.gif")
screen.addshape("car_brown.gif")
screen.addshape("car_cyan.gif")
screen.addshape("car_green.gif")
screen.addshape("car_orange.gif")
screen.addshape("car_pink.gif")
screen.addshape("car_purple.gif")
screen.addshape("car_red.gif")
screen.addshape("car_yellow.gif")
screen.addshape("heart.gif")

# Player Creation
player=p()

# Player Logic
screen.onkey(key="Up",fun=player.forward_fun)
screen.onkey(key="Right",fun=player.turn_right)
screen.onkey(key="Left",fun=player.turn_left)

# Car Creation
CARS=[]
for index in range(0, 30):
    car=c()
    CARS.append(car)

# Scoreboard Creation
scoreboard=sc()

# Line Creation
line=l()

game_on=True
i=1
while game_on:

    screen.tracer(0)
    screen.update()
    time.sleep(0.000000001)
    if i==1:
        for _ in range(0, 3000):
            index = r.randint(0, 9)
            new_car = CARS.pop(index)
            CARS.append(new_car)

            new_car.start_move()
            new_car.is_crash(player)

    if player.LİFE==0:
        game_on=False
        screen.clear()
        end_screen = e()
    index = r.randint(0,9)
    new_car = CARS.pop(index)
    CARS.append(new_car)
    new_car.start_move()
    new_car.is_crash(player)
    i+=1
screen.exitonclick()
