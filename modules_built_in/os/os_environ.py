#!/usr/bin/python3

import os

# list all items
for item, value in os.environ.items():
    print('{} = {}'.format(item, value))

# print one item
print('\n Home =',os.environ['HOME'])
print('\n Home =',os.environ.get('HOME'))