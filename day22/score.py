from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.total_left = 0
        self.total_right = 0
        self.color("white")
        self.goto(0,260)
        self.write_score()

    def write_score(self):
        self.write(f"{self.total_left} : {self.total_right}",False,"center",("Courier",20,"normal"))

    def update_score(self):
        self.clear()
        self.write_score()