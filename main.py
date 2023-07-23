import random
import json
import time


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = []
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Wygenerowane hasło to: {password}")
    is_ok = input("Aby zapisać hasło wpisz 'y': ")
    if is_ok == 'y':
        return password
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
            what_next = input('czy nadpisać hasło? y \nczy zrezygnować? n \n')
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
        # updating old data with new data
        data.update(new_data)

        with open("password.json", "w") as data_file:
            # saving updated data
            json.dump(data, data_file, indent=4)


#-------------------------------------------------------

done = "n"
while done == 'n':
    website = input("Hasło do: ")
    what_next = check(website)

    if what_next =="y":
        my_password = password_generator()
        save_password_to_json(website, my_password)
        print('Hasło zostało zapisane')

    done = input("Koniec na dzisiaj: y\nWygeneruj hasło dla nowego konta: n\n")

print('baj baj')