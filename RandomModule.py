import numpy as np

"""Question 1:
One Random integer
Array of 10 random integers"""
matrix=np.random.randint(1,11)
print(matrix)

"""Question 2:
3×3 random matrix"""

matrix_3x3=np.random.randint(1,11,(3,3))
print("3×3 random matrix"+str(matrix_3x3))

"""Question 3:
  5 random decimal numbers"""

matrix_decimal=np.random.rand(5)
print("5 random decimal numbers"+str(matrix_decimal))

"""seed()
 and generate same random array twice."""

np.random.seed(2)
print(np.random.randint(1,6,5))

"""Question 6:
 [1,2,3,4,5]"""
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)