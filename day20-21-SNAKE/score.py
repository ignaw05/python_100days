from turtle import Turtle



class Score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.high_score = 0
        self.penup()
        self.total = 0
        self.color("white")
        self.goto(0,260)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.total}",False,"center",("Courier",20,"normal"))

    def game_over(self):
        self.goto(0,0)
        if self.score > self.high_score:
            self.high_score = self.score

    def update_score(self):
        self.clear()
        self.total += 1
        self.write_score()
