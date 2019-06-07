#! /usr/bin/python3

from numpy import linspace, sin, cos, exp, pi
import matplotlib.pyplot as mp

# calculate 500 values for x and y without a for loop
x = linspace(0, 10*pi, 500)
y1 = sin(x) * exp(-x/10)
y2 = sin(x)
y3 = cos(x)
y4 = exp(-x/10)

# make diagrams
mp.plot(x,y1)
mp.plot(x,y2)
mp.plot(x,y3)
mp.plot(x,y4)
mp.show()
