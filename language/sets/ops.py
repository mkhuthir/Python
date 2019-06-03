#!/usr/bin/python3

x = {3, 8, 5}
print(x)

x.add(7)
print(x)

x.remove(3)
print(x)

# get length of set x
print(len(x))

# check membership in x
print(5 in x)

# pop random item from set x
print(x.pop(), x)

# delete all items from set x
x.clear()
print(x)
