# Menu

MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
GOOD_SCORE = 50


def main():
    """Execute user's choice from menu options using functions"""
    print(MENU)
    choice = input("Choice: ").lower()
    while choice != 'q':
        if choice == 'g':
            score = int(input("Score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Score: "))
        elif choice == 'p':
            print(determine_category(score))
        elif choice == 's':
            print(show_stars(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").lower()
    print("Goodbye")


def determine_category(score):
    """Determine the category of an entered score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score > EXCELLENT_SCORE:
        return "Excellent"
    elif score > GOOD_SCORE:
        return "Good"
    else:
        return "Bad"


def show_stars(score):
    """Print a number of stars that corresponds to the value of entered score"""
    print("*" * score)


main()
