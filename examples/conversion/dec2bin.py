#!/usr/bin/python3

def decToBin(decNum):
	binNum = 0
	power = 0
	while decNum > 0:
		binNum += 10 ** power * (decNum % 2)
		decNum //= 2
		power += 1
	return binNum

num = 255
print (str(num),"in dec = ", str(decToBin(num)), "in bin")