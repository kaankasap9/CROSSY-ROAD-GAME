from turtle import Turtle
from car import Car
from score import Score

class Player(Turtle):
    STARTİNG_POS = (0, -360)
    STARTİNG_HEADİNG = 90
    DİSTANCE = 22
    LİMİT = [-500, 500]
    LİFE=3
    score=Score()
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(self.STARTİNG_POS)
        self.setheading(self.STARTİNG_HEADİNG)
    def forward_fun(self):
        self.forward(self.DİSTANCE)
        self.next_level()
    def turn_right(self):
        self.setheading(self.heading()-90)
    def turn_left(self):
        self.setheading(self.heading()+90)
    def next_level(self):
        if self.ycor()>400:
            self.goto(self.STARTİNG_POS)
            Car.SPEED+=1
            self.score.increase()
    def crashed(self):
        self.goto(self.STARTİNG_POS)
        self.LİFE-=1
        self.setheading(self.STARTİNG_HEADİNG)
