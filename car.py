from turtle import Turtle as t
import random as r
class Car(t):
    COLORS = ["car_red.gif", "car_blue.gif", "car_yellow.gif", "car_green.gif", "car_pink.gif", "car_orange.gif", "car_cyan.gif", "car_brown.gif", "car_purple.gif"]
    STARTİNG_HEADİNG = 180
    SPEED = 100
    STARTİNG_POS = [(550,-250),(610,-250),(700,-250),(760,-250),(800,-250),(500, -150),(1200, -150),(650, -150),(550, -150), (600, -50),(500, -50),(600, -50), (500, 50), (560, 50), (610, 50), (700, 50), (800, 50), (500,150), (560,150), (610,150), (700,150), (760,150), (850, 250), (700, 250), (900, 250), (950, 250), (1000, 250)]
    LİMİT = -500
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(r.choice(self.STARTİNG_POS))
        self.shape(r.choice(self.COLORS))
        self.setheading(180)
        self.setheading(self.STARTİNG_HEADİNG)
        self.start_move()
    def start_move(self):
        self.forward(self.SPEED)
        self.continuity()
    def continuity(self):
        if self.xcor()<self.LİMİT:
            self.shape(r.choice(self.COLORS))
            self.goto(r.choice(self.STARTİNG_POS))
    def is_crash(self,player):
        if self.distance(player)<30:
            player.crashed()

