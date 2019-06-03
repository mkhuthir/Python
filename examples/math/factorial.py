#! /usr/bin/python3

def get_recursive_factorial(n):
	if n < 0:
		return -1
	elif n < 2:
		return 1
	else:
		return n * get_recursive_factorial(n-1)
		
def get_iterative_factorial(n):
	if n < 0:
		return -1
	else:
		fact = 1
		for i in range(1, n+1):
			fact *= i
		return fact

num = 9		
print("Using Recursive method: factorial of",str(num), "is", get_recursive_factorial(num))
print("Using Iterative method: factorial of",str(num), "is", get_iterative_factorial(num))