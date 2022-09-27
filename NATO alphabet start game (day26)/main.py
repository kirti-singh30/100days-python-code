student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("NATO alphabet start game (day26)/nato_phonetic_alphabet.csv")
#print(data)
alpha_dict ={row.letter:row.code for (index,row) in data.iterrows()}
#print(alpha_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
game_on = True
while game_on:
    user_input = input("Enter a word ")
    try:
        phonetic_code = [alpha_dict[char] for char in user_input.upper()]
    except KeyError:
        print("Sorry, please enter only letters")
    else:
        print(phonetic_code)

