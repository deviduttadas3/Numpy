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

"""Mini Challenge"""
"""Create a fake AI experiment simulator.
Steps:
Set seed
Generate random AI accuracy scores
Run program multiple times
Verify same outputs"""


def run_experiment(run_number):
   
    np.random.seed(50)
    
   
    ai_accuracy_scores = np.random.rand(5) * 100
    
    print(f"Run #{run_number} Scores: {ai_accuracy_scores}")
    return ai_accuracy_scores

def fake_ai_experiment_simulator():
    print("--- Starting Fake AI Experiment Simulator ---")
    
    
    run1 = run_experiment(1)
    run2 = run_experiment(2)
    run3 = run_experiment(3)
    run4 = run_experiment(4)
    run5 = run_experiment(5)
    run6 = run_experiment(6)
    
 
    all_runs = [run1, run2, run3, run4, run5, run6]
    all_match = all(np.array_equal(run1, current_run) for current_run in all_runs)
    
    print("---------------------------------------------")
    print(f"Verification: Are all simulation runs identical? {all_match}")


fake_ai_experiment_simulator()