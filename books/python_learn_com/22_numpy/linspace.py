#! /usr/bin/python

import numpy as np

# linspace ( <startvalue>, <stopvalue>, <number_of_values> )
# logspace ( <startvalue>, <stopvalue>, <number_of_values> )

print 'float linear list:\t', np.linspace(0,5,5)
print '         log list:\t', np.logspace(0.1,1,5)

