#!/usr/bin/python3

import time

# Use time.process_time() to get runtime of an operation on your computer
start_time = time.process_time()

# Do some stuff
print('starting a process')
for i in range(1,10000):
    x =+ i

end_time = time.process_time()
print('operation executed in ', end_time - start_time, 'seconds')