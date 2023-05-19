# Intermediate Exercise: SilverServiceTaxi

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class"""
    my_taxi = SilverServiceTaxi('Silver Prius 1', 100, 2)
    my_taxi.drive(18)
    print(my_taxi.__str__())
    print('current fare = $' + str(my_taxi.get_fare()))


main()
