import numpy as np

"""Question-1:Permute-> [1,2,3,4,5]"""
print("\n---------- The Question -1---------- \n")
def permuted_array():
    matrix=np.array([1,2,3,4,5])
    new_matrix=np.random.permutation(matrix)
    print(f"The Original Matrix Is:{matrix}")
    print(f"The Permuted Matrix Is:{new_matrix}")
permuted_array()
print("\n---------- The Question -2---------- \n")
"""Question-2: Generate permutation from:10 """
def permute_number():
    matrix=np.random.permutation(10)
    print(f"The Permutation From Of 10 Is :{matrix}")
permute_number()
print("\n ---------- Question -3 ----------")
"""Create a 4×2 matrix and permute rows."""
def permute_rows():
    matrix=np.random.randint(
        low=1,
        high=9,
        size=(4,2)
    )
    print(matrix)
    permuted_rows=np.random.permutation(matrix)
    print(f"The Permutaed Rows Matrix Are:\n{permuted_rows}")
permute_rows()

print("\n ---------- question -4 ---------- \n")
"""Permute student names while preserving original array."""
def std():
    name_array=np.random.choice(
             [
                      "Gita Singh",
                      "Lakshmi Biswas",
                      "Saroj Chandra",
                      "Lalita Mandal",
                      "Shanti Chaudhari",
                      "Radha Begam",
                      "Sunita Devi",
                      "Suman Sharma",
                      "Mira Gupta",
                      "Punam Kumar",
                      "Ganesh Vasav",
                      "A Patel",
                      "Sri Kaur",
                      "Gopal Devi",
                      "Naresh Mandal",
                      "Dinesh Raut",
                      "Umesh Singh",
                      "Manoj Prasad",
                      "Vinod Sharma",
                      "Dipak Bai"
                    ],
        size=20,
        replace=False
    )
    print("\n ---------- Printing The Name ----------\n")
    
    print(f"The Original Array_Names Are:\n{name_array}")
    permuted_name_array=np.random.permutation(name_array)
    print("\n ---------- Printing The Permuted Name ----------\n")
    print(f"The Permuted Name Array Is:\n{permuted_name_array}")
std()
"""Question-4 52-card-like array
Then:
permute deck
preserve original deck
print both"""
print("\n ---------- Mini Challenge ---------- \n")
import numpy as np

def Create_Full_Deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck_list = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    deck_matrix = np.array(deck_list)
    return deck_matrix

def Permuted_card_Deck():
    original_deck = Create_Full_Deck()
    shuffled_deck = original_deck.copy()
    np.random.shuffle(shuffled_deck)
    
    print("--- First 5 cards of ORIGINAL Deck ---")
    print(original_deck[:5])
    
    print("\n--- First 5 cards of SHUFFLED Deck ---")
    print(shuffled_deck[:5])

Permuted_card_Deck()
    
    
    
    