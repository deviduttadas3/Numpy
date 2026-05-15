import numpy as np
"""Question 1: Select 5 random values from
[10,20,30,40,50]"""

matrix_1=np.random.choice(
    [10,20,30,40,50],
    size=5
)
print(f"The Choiced Matrix is :{matrix_1}")
"""Question 2: Select 5 random values from:
 [10,20,30,40,50]"""
matrix_2=np.random.choice(
    [10,20,30,40,50],
    size=5
)
print(f"The Choiced Matrix is :{matrix_2}")

"""Question 3.Generate 10 random labels from:

["Cat", "Dog", "Bird"]"""
random_labels=np.random.choice(
    ["Cat","Dog","Bird"],
    size=10
)
print(random_labels)

"""Question 4.Create a fake exam result system:
["Pass", "Fail"]
with probabilities:
80% Pass
20% Fail
Generate results for 50 students."""

result_probabilities=np.random.choice(
    ["Pass", "Fail"],
    size=50,
    p=[0.8,0.2]
)
print(result_probabilities)

print("----------Mini Challenge ----------")
"""Create a fake AI chatbot mood generator.
Possible moods:
["Happy", "Neutral", "Angry", "Excited"]
Generate:
20 random moods
count each mood"""
def fake_AI_chatbot_mood_generator():
    
 possible_mood=np.random.choice(
    ["Happy", "Neutral", "Angry", "Excited"],
    size=20
)
 moods = ["Happy", "Neutral", "Angry", "Excited"]

 for mood in moods:
    print(f"{mood}: {(possible_mood == mood).sum()}")

fake_AI_chatbot_mood_generator()
