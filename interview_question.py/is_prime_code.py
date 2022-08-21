#create a empty class
# class a:
#     pass
# obj = a()
# obj.name = 'xyz'
# print("Name=", obj.name)

num = int(input("Enter your number "))
prime_list = []
def isprime(num):
    m = int(num/2 )+1
    if num > 1:
        for x in range(2,m):
            if num % x == 0:
                return False
                # print(f"{num} is not a prime number")
                # break
        else:
            return True
            #print(f"{num} is a prime number")
    else:
        return False
        #print(f"{num} is not a prime number")

for n in range(num +1):
    if isprime(n):
        prime_list.append(n)

print(prime_list)        