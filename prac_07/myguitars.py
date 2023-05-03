# More Guitars!

from guitar import Guitar

guitars = []

with open("guitars.csv") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)

guitars.sort()

for guitar in guitars:
    print(guitar)


