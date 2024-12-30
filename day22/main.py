from turtle import Turtle,Screen
from Paddle import Paddle
from ball import Ball
import time
from score import Score
time_slice = 0.05
#screen setup
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong pibe")
screen.tracer(0)
screen.listen()

#paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

score = Score()

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

def score_goal():
    ball.start()
    r_paddle.start()
    l_paddle.start()
    score.update_score()

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

#bounce with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

#touch the right paddle
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50:
        ball.touch_r()
        ball.ball_speed -=0.001

#touch the left paddle
    if ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        ball.touch_l()
        ball.ball_speed -= 0.01

#left score
    if ball.xcor() < -380 and l_paddle.distance(ball) > 50:
        score.total_right +=1
        score_goal()

    if ball.xcor() > 380 and r_paddle.distance(ball) > 50:
        score.total_left += 1
        score_goal()

screen.exitonclick()
