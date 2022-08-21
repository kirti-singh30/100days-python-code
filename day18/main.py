from re import T
from turtle import Turtle, Screen
import random
import turtle

timmy = Turtle()
#print(timmy)
timmy.shape("turtle")
#colours = ["green","red","yellow","pink","green","grey","black","coral","skyblue"]
colors_lit = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]
#direction = [0,90,180,270]
turtle.colormode(255)
print(timmy)
#timmy.dot()
#timmy.fd(50)
for y in range(0,5+1):
    timmy.penup()
    timmy.hideturtle()
    #timmy.setposition(-100,-100)
    timmy.setposition(-200,(y*50-100))
    for x in range(0,10):
        timmy.penup() 
        timmy.dot(20,random.choice(colors_lit))
        #timmy.penup()
        timmy.fd(50)
        #timmy.dot(20,'red')

#timmy.position()
#timmy.heading()

#timmy.circle(100)

# def random_color():
#     r = random.randint(0,255)
#     b = random.randint(0,255)
#     g = random.randint(0,255)
#     #new_color = random.choice(r,b,g)
#     return (r,b,g)
    
#timmy.width(10)
timmy.speed("fastest")
# def draw_circle(size):
#     for _ in range(int(360/size)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         head_direction = timmy.heading()
#         timmy.setheading(head_direction + size)
#         timmy.circle(100)
# draw_circle(20)
# for _ in range(250):
#     timmy.forward(30)
#     timmy.width(10)
#     timmy.color(random_color())
#     timmy.setheading(random.choice(direction))


# def shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for side in range(3,11):
#     shape(side)
#     timmy.color(random.choice(colours))
#def random_walk():
    

#for _ in range(15):
    #timmy.forward(10)
    #timmy.penup()
    #timmy.forward(10)
    #immy.pendown()
#for _ in range(4):
    #timmy.forward(100)
    #timmy.right(90)
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
my_screen = Screen()
#my_screen.colormode(255)    
#print(my_screen.canvheight)
my_screen.exitonclick()