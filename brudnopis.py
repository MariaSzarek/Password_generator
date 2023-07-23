# try:
#     file = open("jakis.txt")
#     a_dict = {"key":"value"}
#     print(a_dict['key'])
# except FileNotFoundError:
#     file = open("jakis.txt", 'w')
#     file.write("something")
# except KeyError as sss:
#     print(f"The key {sss} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("cokolwiek co mi sie podoba to jest błąd")


height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("wrong height")


bmi = weight/ height ** 2
print(bmi)

#-------------------------------------------------------

facebook_posts = [
    {"Likes": 1, 'Comments': 1},
    {"Likes": 1, 'Comments': 2, 'Shares': 1},
    {"Likes": 1, 'Comments': 1},
    {"Likes": 1, 'Comments': 1, 'Shares': 1},
]

total_likes = 0

for i in facebook_posts:
    try:
        total_likes += i['Shares']
    except KeyError:
        pass

print(total_likes)

#-------------------------

what_next = input('czy nadpisać hasło? y \nczy zrezygnować? n \n')
if what_next =="y" or what_next =="":
    print('zapisze nowe')
elif what_next =="n":
    print('rezygnuje')