#! /usr/bin/python3


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

for i in frange(0,10,0.5):
	print (i)
