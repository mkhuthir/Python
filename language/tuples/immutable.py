#!/usr/bin/python3

x = (1, 2, 3)
# del(x[1])       # fails
# x[1] = 8        # fails
print(x)

y = ([1, 2], 3)   # a tuple where the first item is a list
del(y[0][1])      # delete the 2
print(y)          # the list within the tuple is mutable
