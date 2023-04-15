# Emails


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        verification = input(f"Is your name {name}? (Y/n) ").upper()
        if verification != "Y" and verification != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} {email}")


def get_name_from_email(email):
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = ""
    for part in parts:
        name += part.capitalize()
    return name


main()










