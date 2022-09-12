from turtle import Turtle,Screen

timmy = Turtle()
def move_forward():
    timmy.fd(10)
def move_backword():
    timmy.back(15)
def counter_clock():
    timmy.heading()
    timmy.lt(20)
def clockwise():
    timmy.heading()
    timmy.rt(25)
def make_circle():
    timmy.circle(50)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
screen = Screen()
screen.listen()
screen.onkey(key="w",fun= move_forward)
screen.onkey(key="s",fun= move_backword)
screen.onkey(key="a",fun= counter_clock)
screen.onkey(key="d",fun= clockwise)
screen.onkey(key="m",fun= make_circle)

screen.onkey(key="c",fun= clear_screen)


screen.exitonclick()