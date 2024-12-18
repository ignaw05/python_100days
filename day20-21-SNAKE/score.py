from turtle import Turtle



class Score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.total = 0
        self.color("white")
        self.goto(0,260)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.total}",False,"center",("Courier",20,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align='center',font=("Courier",30,"normal"))

    def update_score(self):
        self.clear()
        self.total += 1
        self.write_score()
