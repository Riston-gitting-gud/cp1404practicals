"""
Intermediate Exercises - Programming Language
Time started: 10:45
Estimated time for completion: 25 minutes
Actual time taken: 22 minutes
"""


class ProgrammingLanguage:
    """Stores information about a programming language"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representative of a ProgrammingLanguage"""
        return f"({self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year})"

    def is_dynamic(self):
        """Determine if a language is dynamically typed"""
        return self.typing == "Dynamic"



