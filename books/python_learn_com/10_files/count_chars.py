#! /usr/bin/python3

fname = 'romeo.txt'
fhand = open(fname)
ftext = fhand.read()

print('\nNumber of charcters in %s is %d\n' %(fname,len(ftext)))

