def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("which number do you want to check? "))
fibonacci_num = fibonacci(num)
print(f"{fibonacci_num} is your fibonacci number")