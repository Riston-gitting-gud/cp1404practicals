# Intermediate Exercise: SilverServiceTaxi

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1):
        """Initialise a SilverServiceTaxi, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Get the current fare"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of {self.flagfall:.2f} and fanciness of {self.fanciness}"
