#!/usr/bin/python3

import os

print('Listing all files in current directory:...')
for file in os.listdir('.'):
    print(file)

