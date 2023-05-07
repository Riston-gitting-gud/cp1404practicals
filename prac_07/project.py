"""
Project Management Program
Actual time taken: 12 hours
"""

class Project:
    """Project class that stores details about a project"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_estimate, id):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_estimate = completion_estimate
        self.id = id

    def __lt__(self, other):
        """Show if one project is lesser than another in priority"""
        return self.priority < other.priority

    def __gt__(self, other):
        """Show if one project is greater than another in priority"""
        return self.priority > other.priority

    def __le__(self, other):
        """Determine if a project has a lesser than or equal priority to another project"""
        return self.priority <= other.priority

    def __ge__(self, other):
        """Determine if a project has a greater than or equal priority to another project"""
        return self.priority >= other.priority

    def __eq__(self, other):
        """Determine if a project is equal in priority with another project"""
        return self.priority == other.priority

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}," \
               f" cost_estimate: ${self.cost_estimate:.2f}, completion: {self.completion_estimate}%"


