from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :

        scoreboard.reset()
        snake.reset()


    # for seg in snake.segment:
        # if seg == snake.head:
        #     pass
        # elif snake.head.distance(seg) < 10:
        #     game = False
        #     scoreboard.gameover()
    for seg in snake.segment[1:]:
       if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()






screen.exitonclick()

