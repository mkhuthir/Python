#!/usr/bin/python3

# define dict
y = {'fish':25.3, 'beef':33.8, 'chicken':22.7}

# print keys and values
print(y.keys())
print(y.values())

# key-value pairs
print(y.items())

# check membership in y_keys (only looks in keys, not values)
print('beef' in y)

# check membership in y_values
print('clams' in y.values())

