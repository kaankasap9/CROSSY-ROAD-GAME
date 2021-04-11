import turtle as t

class EndScreen(t.Turtle):
    screen=t.Screen()
    end = t.Turtle()
    end.hideturtle()
    style = ('Courier', 20, 'normal')
    def __init__(self):
        self.screen.bgcolor("black")
        self.end.color('red')
        self.end.pendown()
        self.end.write('TURTLE İS DEAD YOU SPEND ALL LİVES', font=self.style, align='center')
