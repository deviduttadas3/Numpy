""" numpy.arange() function creates an array of evenly spaced values within a given interval. It is similar to Python's built-in range() function but returns a NumPy array instead of a list"""
"""-----------------------numpy.arange() function------------------"""
"""The Syntax of numpy.arange() is given below:
   numpy.arange(start, stop, step, dtype=None)"""
"""------------------------Example-------------------------
             Printing  the matrix of 1 to 20...
             it print the matrix length-1 like here is the end point of the matrix is 21 so it print 21-1=20 so your Desired Output is [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
             """

import numpy as np
arr = np.arange(1,21)
print(arr)

