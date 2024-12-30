import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score

#SCREEN SETTINGS
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("EL JUEGO DE LA VIBORITA")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

def start_game():
    screen.resetscreen()

#KEYBOARD MOVEMENTS
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(start_game,"r")


game_is_on = True
t = 0.05
while game_is_on:
    screen.update()
    time.sleep(t)
    snake.move()

    #collisions with food
    if snake.head.distance(food) < 15:
        food.random_pos()
        score.update_score()
        snake.add_tail()
        snake.change_color()

    #collisions with walls
    if -295 > snake.head.xcor() or snake.head.xcor() > 295 or -295 > snake.head.ycor() or snake.head.ycor() > 295:
        score.game_over()
        game_is_on = False

    #collision with tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            score.game_over()
            game_is_on = False



screen.exitonclick()