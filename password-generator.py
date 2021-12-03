from random import sample
import json
from os import remove
# Using the ascii table, it's possible to see that the chars begin 32 and end in 126 #
characters = [chr(x) for x in range(32, 127)]
filename = "passwords.json"


def menu():
    option = int(input("-------------------------\n[1] Search password.\n[2] Insert password.\n[3] Remove password\n[4] Remove ALL passwords\n[0] Exit.\n-> "))

    if option == 0:
        return False

    elif option == 1:
        key = input("Which app your passwords is associed?\n-> ")
        search(key)
        return True

    elif option == 2:
        key = input("Which app will associate with the password?\n-> ")
        insert(key)
        return True

    elif option == 3:
        key = input("Which app will associate with the password?\n-> ")
        delete(key)
        return True

    elif option == 4:
        delete_all()
        return True

    else:
        print(">>>>>>>>>>Invalid Choice<<<<<<<<")
        return True


def dump_json(passwords):
    try:
        with open(filename, "w") as json_file:
            json.dump(passwords, json_file)
    except Exception as error:
        print(error)


def load_json():
    try:
        with open(filename, "r") as json_file:
            passwords = json.load(json_file)
            return passwords
    except Exception as error:
        print(f"Don`t have passwords: {error}")


def search(key):
    passwords = load_json()
    try:
        print(f"Your password of {key} is this: {passwords[key]}")

    except:
        if passwords:
            print("The app is not associated in something password!")


def insert(key):
    passwords: dict
    try:
        passwords = load_json()
    except:
        print("This is your first password, tks for to use the app!")

    if type(passwords) is not dict:
        passwords = {}

    if key in passwords.keys():
        choice = input(f"Are you sure you want to change the password of the {key}? Yes or No.\n-> ")
        if choice not in ("y", "Y", "Yes", "yes", "YES"):
            return

    password = "".join(sample(characters, 15))
    print(f"Your password is this: {password}")

    passwords[key] = password

    dump_json(passwords)


def delete(key):
    passwords: dict
    try:
        passwords = load_json()
    except:
        print("You never inserted password!")
        return

    if key in passwords:
        passwords.pop(key)
        dump_json(passwords)
        print(f"The password of {key} has deleted")
    else:
        print("Don`t have any password associate in the {key}")


def delete_all():
    choice = input('Are you sure? Yes or No\n-> ')
    if choice in ('y', 'Y', 'Yes', 'yes', 'YES'):
        remove(filename)


def main():
    _continue = True
    while _continue:
        _continue = menu()


if __name__ == "__main__":
    main()
