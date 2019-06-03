#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-22/7, 22/7, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
