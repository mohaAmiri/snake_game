import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

""" screen setup """
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("snake game")
screen.tracer(0)

""" create objects """
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.welcome()

""" listen to keys to start and change direction """
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def start_game():
    scoreboard.welcome_message.clear()
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        """ detect collision with food and increase score """
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        """ detect collision with borders """
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()
            scoreboard.welcome()
            break

        """ detect collision with the snake itself """
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                scoreboard.welcome()
                return


""" start on enter and quit on click """
screen.onkey(start_game, "Return")
screen.exitonclick()
