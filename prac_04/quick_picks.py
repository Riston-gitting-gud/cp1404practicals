# "Quick Pick" Lottery Ticket Generator

import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45



def main():
    """Quick picks of random numbers"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number")
        number_of_quick_picks = int(input("How manu quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print("".join(f"{number:2}" for number in quick_pick))   # format each number and join them into a single string


main()


