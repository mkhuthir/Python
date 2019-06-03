#! /usr/bin/python3

try:

#	a=1/0
	a=int('Hello')
	
	print('No error happen')
	



except ZeroDivisionError:

	print('Divison by Zero Error !')

except ValueError:

	print('Wrong value Error !')

except:

	print('Other type of error!!')
