# Password Stars

MINIMUM_LENGTH = 5


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(MINIMUM_LENGTH):
    password = input(f"Enter a number that is at least {MINIMUM_LENGTH} characters:  ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short.")
        password = input(f"Enter a number that is at least {MINIMUM_LENGTH} characters:  ")
    return password


def print_asterisks(sequence):
    print("*"*len(sequence))


main()
