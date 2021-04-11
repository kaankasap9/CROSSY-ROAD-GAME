import turtle as t
import time
class Score():
        SCORE = 1
        scoreboard = t.Turtle()
        scoreboard.hideturtle()
        style = ('Courier', 20, 'normal')
        title_style = ('Courier', 30, 'normal')
        scoreboard.write(f'CROSSY ROAD POWERED by KAAN', font=title_style, align='center')
        time.sleep(2)
        def __init__(self):
            self.scoreboard.clear()
            self.scoreboard.penup()
            self.scoreboard.goto(350, 360)
            self.scoreboard.pendown()
            self.scoreboard.write(f'LEVEL : {self.SCORE} ', font=self.style, align='center')
        def increase(self):
            self.scoreboard.clear()
            self.SCORE+=1
            self.scoreboard.write(f'LEVEL : {self.SCORE} ', font=self.style, align='center')