import random
from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title= "make your bet",prompt= " which turtle win the race? Enter a color")
colors = ['red','orange', 'yellow','green','purple','blue']
y_position =[-100,-70,-40,-10,20,50]
all_turtle = []
#print(user_bet)
#timmy = Turtle(shape= "turtle")
for i in range(0,6):
    new_turtle = Turtle(shape= "turtle")
    #timmy.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y =y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have win. the winning color is {winning_color}")
            else:
                print(f"you have loose. the winning color is {winning_color}")

        round_distance = random.randint(0,10)
        turtle.forward(round_distance)

#timmy.penup()
#timmy.goto(x = -230,y =-100)
screen.exitonclick()
