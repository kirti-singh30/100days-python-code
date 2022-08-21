# from turtle import Turtle, Screen
# #from prettytable import PrettyTable
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.align = "l"

print(table)