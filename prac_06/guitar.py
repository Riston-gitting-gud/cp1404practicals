"""
Do-from-scratch Exercises - Guitars!
Time started: 19:38
Estimated time for completion: 45 minutes
Actual time taken: 43 minutes
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Guitar class that stores details about a guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar"""
        self.name = name
        self.year = year
        self.cost = cost
        print(f"My guitar: {name}, first made in {year}")

    def __str__(self):
        """Return a string representation of a Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on CURRENT_YEAR"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Show the difference of years between Guitars"""
        return self.year < other.year
