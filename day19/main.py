import random
import turtle
from turtle import Turtle,Screen

t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")
t6 = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500,height=400)


colors = ['green','purple','blue','pink','red','orange']
turtles = [t1,t2,t3,t4,t5,t6]
j = -70
k = 0
winner = None
coord = 0

for i in turtles:
    i.penup()
    i.color(colors[k])
    i.goto(-240,j)
    j +=30
    k +=1

user_answer = screen.textinput("Make your bet!","Which color will win?")

while winner is None:
    for t in turtles:
        t.forward(random.randint(0,10))
        coord = t.xcor()
        if coord >= 220.0:
            winner = t.getturtle()
            break
print(winner.pencolor())

if user_answer == winner.pencolor():
    print("You won")
else: print("You lost")
screen.exitonclick()