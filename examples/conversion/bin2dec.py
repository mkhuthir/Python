#!/usr/bin/python3

def binToDec(binNum):
	decNum = 0
	power = 0
	while binNum > 0:
		decNum += 2 ** power * (binNum % 10)
		binNum //= 10
		power += 1
	return decNum

num = 11111110	
print (str(num), " in bin = ",str(binToDec(num)), "in dec")
