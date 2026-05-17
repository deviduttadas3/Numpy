import numpy as np
"""1.Shuffle:
[1,2,3,4,5,6,7,8]"""
def question1():
    
 matrix=np.arange(1,9)
 print(matrix)
 np.random.shuffle(matrix)
 print(f"Shuffled Matrix : {matrix}")
question1()
"""2.Create a random integer array and shuffle it."""
import numpy as np

"""2.Create a random integer array and shuffle it."""

def question2():
    matrix = np.random.randint(
        low=10,
        high=51,
        size=(3,3)
    )
    print("Original Matrix:")
    print(matrix)
    flatten_matrix = matrix.flatten()
    np.random.shuffle(flatten_matrix)
    reshaped_matrix = flatten_matrix.reshape(3,3)
    print("\nShuffled Matrix:")
    print(reshaped_matrix)

question2()

"""3.Create a 4×2 matrix and shuffle rows."""

def question3():
    matrix=np.random.randint(
        low=1,
        high=50,
        size=(4,2)
    )
    print("Original Matrix:")
    print(matrix)
    flatten_matrix=matrix.flatten()
    np.random.shuffle(flatten_matrix)
    reshaped_matrix= flatten_matrix.reshape(4,2)
    print("\nShuffled Matrix:")
    print(reshaped_matrix)
   
question3()

"""4.Shuffle a list of student names."""

def std_names():
    std_name_matrix=np.array(["Krishna","Rahul","Rohit","Hari","Gopal"])
    np.random.shuffle(std_name_matrix)
    print(f"The Shuffled Name Matrix:{std_name_matrix}")
    
std_names()

