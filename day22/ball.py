from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.ball_speed = 0.05
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1

    def touch_r(self):
        self.x_move = -(abs(self.x_move))

    def touch_l(self):
        self.x_move = abs(self.x_move)

    def start(self):
        self.goto(0,0)
        self.x_move *= -1
        self.ball_speed = 0.05
        self.y_move *= -1

