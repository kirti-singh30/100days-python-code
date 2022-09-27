from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "u")
screen.onkey(l_paddle.down, "d")
game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    #detection the collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()
    #detection with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()

    #detection ball bounce from right paddle
    if ball.xcor()>380:
        ball.reset_postion()
        scoreboard.l_point()
    #detection ball bounce from left paddle
    if ball.xcor() < -380:
        ball.reset_postion()
        scoreboard.r_point()


screen.exitonclick()