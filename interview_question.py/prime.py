num = int(input("enter number"))
m = int(num/2)+1
# If given number is greater than 1
if num > 1:

	# Iterate from 2 to n / 2
	for i in range(2,m):

		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(f"{num} is not a prime number")
			break
	else:
		print(f"{num} is a prime number")

else:
	print(f"{num}is not a prime number")
