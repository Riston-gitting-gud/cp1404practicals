# Question 3: Loops

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.

stars_count = int(input("Number of stars: "))
for i in range(stars_count):
    print('*', end=' ')
print()

# d.

stars_count = int(input("Number of stars: "))
for i in range(1, stars_count + 1):
    print('*' * i)
print()



