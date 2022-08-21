from turtle import Turtle,Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("snake_game")
screen.tracer(0)
turtle = Turtle()
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    #game_on = False

















screen.exitonclick()