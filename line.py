import turtle as t

LİNE_POS = [(470, -300), (470, -200), (470, -100), (470, 0), (470, 100), (470, 200), (470, 300)]
class Line(t.Turtle):
    def __init__(self):
        self.line()

    def line(self):
        for pos in LİNE_POS:
            t.hideturtle()
            t.pencolor("white")
            t.pensize(3)
            t.penup()
            t.goto(pos)
            t.setheading(180)
            t.pendown()
            for i in range(0, 10):
                t.forward(50)
                t.penup()
                t.forward(50)
                t.pendown()
