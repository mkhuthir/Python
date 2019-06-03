#! /usr/bin/python3
	
# Name Error type in except block
# call function from try block.

def this_fails():
	x = 1/0

try:
	this_fails()

except ZeroDivisionError as err:
	print('Handling run-time error:', err)