"""
Do-from-scratch Exercises - Guitars!
Time started: 19:38
Estimated time for completion: 45 minutes
Actual time taken: 43 minutes
"""

from guitar import Guitar

CURRENT_YEAR = 2023


def run_tests():
    """Tests Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1539.6)

    print(f"{guitar.name} get_age() - Expected {101}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {10}. Got {other.get_age()}")
    print()
    print(f"{other.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_tests()
