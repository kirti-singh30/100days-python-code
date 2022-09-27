# import tkinter
# from turtle import Screen

# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)

# #label (creating some componetn inside the window)

# my_label = tkinter.Label(text = "I am the label",font=("Aerial",24, "bold"))
# my_label.pack(side="bottom")
# my_label.pack(expand=True)

## altenative 
from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#label (creating some componetn inside the window)

my_label = Label(text = "I am the label",font=("Aerial",24, "bold"))
my_label.grid(column=0,row=0)

my_label["text"] = "New Text"
my_label.config(text= "New Text")
# buttons
button = Button(text="click me", command=button_clicked)
button.grid(column=1,row=1)


new_button = Button(text="click new button")
new_button.grid(column=2,row=0)

#entry
input = Entry(width=12)
input.grid(column=3,row=2)









window.mainloop()