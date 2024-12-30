import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('orange')
        self.speed("fastest")
        self.random_pos()


    def random_pos(self):
        pos = random.randint(-280,280)
        self.goto(pos,pos)