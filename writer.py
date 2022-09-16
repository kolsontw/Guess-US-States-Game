from turtle import Turtle
FONT = ("Courier", 8, "normal")

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def wr(self, name, x, y):
        self.goto(x, y)
        self.write(name, False, "Center", FONT)
