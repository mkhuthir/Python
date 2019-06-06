#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
	print('Number of arguments  :', len(sys.argv))
	print ('Argument List       :', str(sys.argv))
	print('Argument number 2 is :', sys.argv[1])
else:
	print('You did not supply any argument')

