#! /usr/bin/python3

fname='output.txt'
fhand=open(fname,'w')

fhand.write('This is the first line in file\n')
fhand.write('This is the second line in file\n')
fhand.write('This is the third line in file\n')

fhand.close()
print('Created file:%s' %fname)
