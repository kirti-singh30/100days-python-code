from turtle import Turtle
X_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENTS = 20
UP = 90
DOWN =270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):    
        for i in X_POS:
            self.add_segment(i)

    def add_segment(self,i):
        new_snake = Turtle(shape= "square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(i)
        self.all_snake.append(new_snake)

    def extend(self):
        self.add_segment(self.all_snake[-1].position())


    def reset(self):
        for seg in self.all_snake:
            seg.goto(1000,1000)
        self.all_snake.clear()
        self.create_snake()
        self.head = self.all_snake[0]



    def move_snake(self):
        for snk in range(len(self.all_snake)-1,0,-1): # to change the square position 
            new_x = self.all_snake[snk-1].xcor()
            new_y = self.all_snake[snk-1].ycor()
            self.all_snake[snk].goto(new_x,new_y)
        self.all_snake[0].fd(MOVEMENTS)
        #self.all_snake[0].left(90)


    def up(self):
        if self.all_snake[0].heading() != DOWN:
            self.all_snake[0].setheading(UP)
            
    def down(self):
        if self.all_snake[0].heading() != UP:
            self.all_snake[0].setheading(DOWN)

    def left(self):
        if self.all_snake[0].heading() != RIGHT:
            self.all_snake[0].setheading(LEFT)
        
    def right(self):
        if self.all_snake[0].heading() != LEFT:
            self.all_snake[0].setheading(RIGHT)
