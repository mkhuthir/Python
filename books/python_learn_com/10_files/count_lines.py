#! /usr/bin/python3

fname = 'romeo.txt'
fhand = open('romeo.txt')
count = 0

for line in fhand:
	count = count + 1

print ('\nNumber of lines in %s is %d\n' %(fname,count))
