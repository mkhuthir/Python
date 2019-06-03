#!/usr/bin/python3

# define dict x
x = {'fish':25.3, 'beef':33.8, 'chicken':22.7}
print(x)

# add or update
x['shrimp'] = 38.2
print(x)

# delete an item
del(x['shrimp'])
print(x)

# get length of dict x
print(len(x))

# delete all items from dict x
x.clear()
print(x)

# delete dict x
del(x)
