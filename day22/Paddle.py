from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.goto(pos)
        self.speed("fastest")
        self.starting_pos = self.pos()
    def up(self):
        self.goto(self.xcor(),self.ycor()+20)


    def down(self):
        self.goto(self.xcor(),self.ycor()-20)

    def start(self):
        self.goto(self.starting_pos)