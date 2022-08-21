def prime_num(x,y):
    prime_list = []
    for i in range(x,y):
        if i== 0 or i == 1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_num = 15
ending_num = 67
new_prime_list = prime_num(starting_num,ending_num)
if len(new_prime_list) == 0:
    print("there is no prime number between in this range")

else:
    print(f"there is the prime number in this range {new_prime_list}")

