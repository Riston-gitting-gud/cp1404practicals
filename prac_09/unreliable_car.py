# Intermediate Exercise: UnreliableCar

from car import Car
import random


class UnreliableCar(Car):
    """An unreliable version of a Car"""

    def __init__(self, name, fuel, reliability=0):
        """Initialise an UnreliableCar, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car depending on reliability"""
        reliability_check = random.randint(1, 100)
        if self.reliability < reliability_check:    # Check for reliability
            print('Car did not drive. Reliability check failed.')
            distance_driven = 0
        else:   # Drive like a reliable parent Car
            distance_driven = super().drive(distance)
        return distance_driven
