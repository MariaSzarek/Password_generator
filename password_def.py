import random
import json
import time
import string


def password_generator():

    password_letters = random.choices(string.ascii_letters, k=random.randint(8, 10))
    password_symbols = random.choices(string.punctuation, k=random.randint(2, 4))
    password_numbers = random.choices(string.digits, k=random.randint(2, 4))

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Wygenerowane hasło to: {password}")
    is_ok = input("Aby zapisać hasło wpisz 'y', aby przerwać 'n': ")
    if is_ok == 'y':
        return password
    elif is_ok == 'n':
        return None
    else:
        print("Nie zapisano hasła.")
        time.sleep(1)
        print("Zaraz otrzymasz nowe hasło")
        time.sleep(1)
        return password_generator()


def check(website):
    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        return 'y'

    else:
        if website in data:
            print(f'Istnieje już hasło dla konta {website}')
            what_next = input('Czy nadpisać hasło? y \nCzy zrezygnować? n \n')
            return what_next
        else:
            return 'y'


def save_password_to_json(website, password):
    new_data = {
        website : password
    }

    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        with open("password.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
        data.update(new_data)

        with open("password.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

