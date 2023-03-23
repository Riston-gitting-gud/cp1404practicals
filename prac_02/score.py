# Scores

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
GOOD_SCORE = 50


def main():
    """Get score and determine its category"""
    score = float(input("Enter score: "))
    print(determine_category(score))


def determine_category(score):
    """Determine the category of a score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score > EXCELLENT_SCORE:
        return "Excellent"
    elif score > GOOD_SCORE:
        return "Good"
    else:
        return "Bad"


main()
