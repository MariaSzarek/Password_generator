
import random
import json

#---PASSWORD GENERATOR--#
website = ""

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
        return password_generator()


def save_password_to_json(password):
    data = {
        "website": website,
        "password": password
    }

    with open("password.json", "w") as json_file:
        json_file.write(f"{data['website']}: {data['password']}\n")



website = input("Hasło do: ")

my_password = password_generator()
print(f"Twoje hasło: {my_password}")

save_password_to_json(my_password)
print('Hasło zostało zapisane')