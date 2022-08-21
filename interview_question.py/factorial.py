#import math
 
#def factorial(n):
    #return(math.factorial(n))
 
 # Python 3 program to find
# factorial of given number
def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1);

# Driver Code
num = 11
facto_num = factorial(num)
print(f"Factorial of this {num} is {facto_num}") 
# This code is contributed by Smitha Dinesh Semwal
