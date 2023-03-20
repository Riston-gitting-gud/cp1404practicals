# Question 2: Debugging

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
GOOD_SCORE = 50
score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid score")
elif score > EXCELLENT_SCORE:
    print("Excellent")
elif score > GOOD_SCORE:
    print("Good")
else:
    print("Bad")
