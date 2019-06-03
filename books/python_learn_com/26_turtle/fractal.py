#! /usr/bin/python

import time
from turtle import *

up()
backward(200)
down()
 
def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
 
f(550, 4)

time.sleep(5)
