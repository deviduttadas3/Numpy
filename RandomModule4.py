import numpy as np

"""Question 1.Set seed to:
42
Then generate 5 random integers.

Run multiple times and observe output."""
def generate_5_random_matrix():
    np.random.seed(42)
    matrix=np.random.randint(
        low=1,
        high=6,
        size=5    
    )
    print(matrix)
generate_5_random_matrix()

"""Question 2. Set seed to:
100
Generate:
a 3×3 random integer matrix
a 3×3 decimal matrix using rand()"""

def generate_3x3_matrix():
    np.random.seed(100)
    integer_matrix=np.random.randint(
        low=10,
        high=51,
        size=(3,3)
    )
    decimal_matrix=np.random.rand(
        3,3
    )
    
    print(integer_matrix)
    print(decimal_matrix)
generate_3x3_matrix()

"""Question 3. Use Seed Twice and Prove OutPuts are Identical...."""

def identical_output():
    np.random.seed(2)
    matrix_1 = np.random.randint(low=1, high=6, size=(3, 3))
    
    np.random.seed(2)
    matrix_2 = np.random.randint(low=1, high=6, size=(3, 3))
    
    print("Matrix 1:")
    print(matrix_1)
    print("\nMatrix 2:")
    print(matrix_2)
    
    are_identical = np.array_equal(matrix_1, matrix_2)
    print(f"\nAre both matrices identical? {are_identical}")

identical_output()

