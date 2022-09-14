##TODO: Create a letter using starting_letter.txt 

# with open("day24_Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
#     letter_file = file.readlines()
    
# ##for each name in invited_names.txt

# with open("day24_Mail Merge Project Start/Input/Names/invited_names.txt") as f:
#     name_file = f.readlines()

# for nam in name_file:
#     nam_letter = letter_file.copy()
#     nam_letter[0] = nam_letter[0].replace("[name]",nam.strip())
#     with open(f'day24_Mail Merge Project Start/readytosend_{nam}_.txt', 'w') as output_file:
#         for letter in nam_letter:
#             output_file.write(letter)

""" alternative solution """

PLACEHOLDER = "[name]"

with open("Mail Merge Project Start(day24)/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    #print(letter_content)

with open("Mail Merge Project Start(day24)/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,strip_name)
        with open(f"Mail Merge Project Start(day24)/Output/ReadyToSend {strip_name}.txt","w") as complete_letter:
            complete_letter.write(new_letter)
            

