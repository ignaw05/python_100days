import colorgram
import turtle as t
import random

colors = colorgram.extract('/Users/ignaciowuilloud/Downloads/hirst.webp',45)
t.colormode(255)

timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r,g,b))


for k in range (0,500,50):
    for j in range(0,500,50):
        timmy.setposition((j-200,k-100))
        timmy.dot(20,random.choice(color_list))

timmy.hideturtle()
