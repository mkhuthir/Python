#! /usr/bin/python3

fname1 = 'romeo.txt'
fname2 = 'romeo_words.txt'
fhand1 = open(fname1)
fhand2 = open(fname2,'w')

wordList=[]

for line in fhand1:
	words=line.split()
	for word in words:
		if not (word in wordList):
			wordList.append(word)
			
wordList.sort()

for word in wordList:
	fhand2.write(word+'\n')
	
fhand2.close()

print('Created file %s containing all words from file %s'%(fname1,fname2))
