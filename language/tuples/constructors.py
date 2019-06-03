#!/usr/bin/python3

x = ()
print(x)

x = (1, 2, 3)
print(x)

x = 1, 2, 3
print(x)

# the comma tells Python it's a tuple
x = 2,
print(x)

list1 = [2, 4, 6]
x = tuple(list1)
print(x)

print(type(x))

