import random
from art import logo, vs
from game_data import data
print(logo)

a = random.randint(0,len(data))
b = random.randint(0,len(data))
first_person_data = data[a]
second_person_data = data[b]

first_value_a = first_person_data['name']
sec_value_a = first_person_data['description']
third_value_a = first_person_data['country']
forth_value_a = first_person_data['follower_count']
#print(f"compare A : {first_value_a}, {sec_value_a},{third_value_a}")
#print(vs)

first_value_b = second_person_data['name']
sec_value_b = second_person_data['description']
third_value_b = second_person_data['country']
forth_value_b = second_person_data['follower_count']
#print(f"Againts B : {first_value_b}, {sec_value_b},{third_value_b}")


game_on = True
score = 0
while game_on:
  print(f"compare A : {first_person_data['name']}, {first_person_data['description']},{first_person_data['country']}")
  print(vs)
  print(f"Againts B : {second_person_data['name']}, {second_person_data['description']},{second_person_data['country']}")
  user_inp = input("who has more followers? Type 'A' or 'B': ")
  if first_person_data['follower_count'] > second_person_data['follower_count']:
    answer = 'A'
  else:
    answer = 'B'
  if user_inp == answer:
    score += 1
    print(f"you are write.Your score is {score}")
    first_person_data = second_person_data
    b = random.randint(0,len(data))
    second_person_data = data[b]
  else:
    print(f" sorry that is wrong.Your score is {score}")
    game_on = False

  
  
  



