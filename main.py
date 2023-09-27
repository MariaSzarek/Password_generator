from password_def import *
from art import logo

print(logo)
done = "n"
while done == 'n':
    website = input("Hasło do: ")
    what_next = check(website)

    if what_next =="y":
        my_password = password_generator()
        if my_password == None:
            print("Hasło nie zostało zapisane")
        else:
            save_password_to_json(website, my_password)
            print('Hasło zostało zapisane')

    done = input("Koniec na dzisiaj: y\nWygeneruj hasło dla nowego konta: n\n")

print('Baj Baj')