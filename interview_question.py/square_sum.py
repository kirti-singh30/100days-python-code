def squaresum(n) :
	sm = 0
	for i in range(1, n+1) :
		sm = sm + (i * i)
	
	return sm

# Driven Program
num = int(input("which number do you want to check?"))
nat_sqr_num = squaresum(num)
print(f"this is the natural number {nat_sqr_num}")

