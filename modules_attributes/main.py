#!/usr/bin/python3

def fibo(n):
    """Fibonacci series module"""
    FiboList=[]
    a,b=0,1
    while b<n:
        FiboList.append(b)
        a, b = b, a+b
    return FiboList

# the following will run only when script is called directly (not imported as a module)
if __name__== "__main__":
    print (fibo.__doc__)
    print ("Fibonacci series", fibo(100))



