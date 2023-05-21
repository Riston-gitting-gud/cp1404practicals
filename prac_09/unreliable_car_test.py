# Intermediate Exercise: UnreliableCar

from unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars"""
    good_car = UnreliableCar("Better-than-average Volvo XC60", 100, 50)
    bad_car = UnreliableCar("Suspicious Unknown Model Found Near The Junkyard", 100, 9)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name} drove {good_car.drive(i)}km")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km")

    print(good_car)
    print(bad_car)


main()
