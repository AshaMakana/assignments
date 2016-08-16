def recursive_factorial(n):
	if n == 1:
		return 1
	else:
		return(n* recursive_factorial(n-1))

def iterative_factorial(n):
	result = 1
	for i in range(1, n+1):
		result *= i 
	return result

	

print (iterative_factorial(4))
print (recursive_factorial(4))
