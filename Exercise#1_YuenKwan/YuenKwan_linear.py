# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:50:59 2023

@author: YuenKwan LI (301228849)
"""

import numpy as np
import matplotlib.pyplot as plt

# Req.b: Set random seed
np.random.seed(49)

# Req.a: Generate 100 random numbers from a uniform distribution between -10 and 10
x = np.random.uniform(low= -10, high= 10, size= 100)

# Req.c: Generate y data using x data
y = 12 * x - 4

# Req.d: Generate scatter plot of x and y
plt.scatter(x, y, alpha=0.5)
plt.title("Scatter plot of x and y")
plt.xlabel("x")
plt.ylabel("y")
plt.rcParams['figure.dpi'] = 300
plt.show()

# Req.e: Add noise to y from a normal distribution with mean=0 and standard deviation=1
noise = np.random.normal(loc= 0, scale= 1, size= 100)
y = (12 * x - 4) + noise

# Req.f: Generate scatter plot of x and y with noise
plt.scatter(x, y, alpha=0.5)
plt.title("Scatter plot of x and y (with noise)")
plt.xlabel("x")
plt.ylabel("y")
plt.rcParams['figure.dpi'] = 300
plt.show()

'''
The plot without noise shows a clear linear relationship between x and y.
The plot with noise has a scatter of points around the line. It is because noise injected to y.
'''