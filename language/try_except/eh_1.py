#! /usr/bin/python3

filename = 'exception_data.txt'

# Outer try block catches file name or file
# doesn't exist errors.

try:
	with open(filename) as fin:
		for line in fin:
			print('\nline: ',line,end='')
			items = line.split(',')
			total = 0

			# Inner try bock catches integer conversion errors.
			try:
				for item in items:
					num = int(item)
					total += num
			
				print('Total = ' + str(total))

			except:
				print('Error converting to integer: ', items)

			else:
				print('there was no error in conversion.')

except:
	print('Error opening file. ' + filename)

finally:
	print('\nThis is our optional finally block. Code here will execute no matter what.')
