import turtle
import pandas
screen = turtle.Screen()
screen.title("US_State_game")
image = "day25_us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#answer_state = screen.textinput(title= "Guess the state", prompt= "what is the another state name").capitalize()
#print(answer_state)

data = pandas.read_csv("day25_us-states-game-start/50_states.csv")
all_states = data["state"].to_list()
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title= f"{len(guess_state)}/50", prompt= "what is the another state name").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        new_data = data[data.state == answer_state]
        t.goto(new_data.x.values[0],new_data.y.values[0])
        t.write(answer_state)

state_to_learn = list(set(all_states)- set(guess_state))
print(state_to_learn)
data = pandas.DataFrame(state_to_learn)
data.to_csv("state_to_learn.csv")

