"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ValueError occurs when the user inputs a string instead of an integer.

2. When will a ZeroDivisionError occur?
ZeroDivisionError occurs when the user inputs a number divided by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes. I can set up an error checking while loop for the user's input for the denominator
such that if the user enters zero, he/she will be prompted to re-enter a number that is not zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero. Enter Again.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
