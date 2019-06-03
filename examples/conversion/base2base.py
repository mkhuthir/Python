#!/usr/bin/python3

def convert(fromNum, fromBase, toBase):
	toNum = 0
	power = 0
	while fromNum > 0:
		toNum += fromBase ** power * (fromNum % toBase)
		fromNum //= toBase
		power += 1
	return toNum

print ("127 from base 10 to base 8 :", str(convert(127, 10, 8)))
print ("1001 from base 2 to base 10 :", str(convert(1001, 2, 10)))