# Password Stars

MINIMUM_LENGTH = 5


def main():
    """Get password and print it using functions"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(MINIMUM_LENGTH):
    """Get password of a minimum length"""
    password = input(f"Enter a number that is at least {MINIMUM_LENGTH} characters:  ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short.")
        password = input(f"Enter a number that is at least {MINIMUM_LENGTH} characters:  ")
    return password


def print_asterisks(sequence):
    """Print the same number of asterisks as the number of characters in password"""
    print("*"*len(sequence))


main()
