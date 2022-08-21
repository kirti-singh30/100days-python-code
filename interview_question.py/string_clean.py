#from curses.ascii import isdigit
from os import remove


ini_string = "Geeks123for127geeks"
new_string = " "
for char in ini_string:
    if not char.isdigit():
        new_string += char
       
print(f"this is the new string {new_string}")