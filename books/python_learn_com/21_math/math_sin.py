#! /usr/bin/python3

import math

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

for i in frange(-math.pi, math.pi, 0.2):
    print('i={0:+f}\tsin={1:+f}\tcos={2:+f}'.format(i, math.sin(i), math.cos(i)))

