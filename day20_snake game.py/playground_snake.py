from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("snake_game")
snake = Turtle()

start_pos = [(0,0),(-20,0),(-40,0)] # here use of tupleto get the position of the square
segments = []
for pos in start_pos:
    new_snake = Turtle("square")
    new_snake.color("white")
    new_snake.goto(pos)

game_on = True
while game_on:


























screen.exitonclick()