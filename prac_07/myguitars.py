# More Guitars!

from guitar import Guitar


def main():
    """Guitar program that uses the class Guitar"""
    guitars = load_guitars()
    while True:
        name = input("Enter your guitar name: ")
        if not name:
            print("These are your guitars!")
            break
        year = input("Enter the year the guitar was made: ")
        cost = input("Enter the cost of the guitar: $")
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)

    guitars.sort()
    save_guitars(guitars)


def load_guitars():
    """Loads the csv file containing guitars"""
    guitars = []

    with open("guitars.csv") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)

    return guitars


def save_guitars(guitars):
    """Saves the updated guitars to the csv file"""
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}" + "\n")


main()
