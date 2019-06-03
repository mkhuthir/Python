#! /usr/bin/python3

print('\nHello my friend!!')
i=input("Input a decimal number ? (anything else to quit) ")

while i.isdecimal():

	if int(i)<9:
		print('input is less than 9')
	elif int(i)>9:
 		print('input is more than 9')
	else:
		print('Your input was 9!!!')

	i=input("Input another decimal number ? (anything else to quit) ")
	
print('\nSee you....\n')
