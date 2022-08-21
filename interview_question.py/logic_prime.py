# we want to check list of prime numbers
from operator import ne


def prime_num(x,y):
    prime_list = []
    for i in range(x,y):
        if i == 0 or i ==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_range = 15
ending_range = 89
new_prime_list = prime_num(starting_range,ending_range)
if len(new_prime_list) == 0:
    print(" with this range there is no prime number")
else:
    print(f"with this range the prime number list is {new_prime_list}")