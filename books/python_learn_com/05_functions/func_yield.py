#! /usr/bin/python3

def myFunc(a):
	while a>0:
		yield a*a
		a=a-1


for i in myFunc(10):
	print(i)
