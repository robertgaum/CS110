x = 2
y = "2"
z = True

if type(x) is int:
    print("Integer")
if type(y) is str:
    print("String")
if type(z) is bool:
    print("Boolean")

if (True or True and False):
    print("True")
else:
    print("False")

if ((True and False) and (True or False) or (False and False)):
    print("True")
else:
    print("False")

if (5 >= 5 and 2 is 2):
    print("True")
else:
    print("False")

if 2 in [1,3,5,7,9]:
    print("True")
else:
    print("False")

if (7 > 3 + 3):
    print("True")
else:
    print("False")

#This variable will trigger whenever the user enters an item that is not in the list
error = False

print("Pick your favorite animal from: Tiger, Lion, Fish")
animal = input().lower()
if animal not in ('tiger', 'lion', 'fish'):
    error = True

print("Pick your favorite color from: Red, Blue, Purple")
color = input().lower()
if color not in ('red', 'blue', 'purple'):
    error = True

animalChoice = ""
colorChoice = ""

if animal == 'tiger':
    animalChoice = 'tiger'

    if color == 'red':
        colorChoice = 'red'
    elif color == 'blue':
        colorChoice = 'blue'
    elif color == 'purple':
        colorChoice = 'purple'
    else:
        print("Error - An unknown error has occured.")

elif animal == 'lion':
    animalChoice = 'lion'

    if color == 'red':
        colorChoice = 'red'
    elif color == 'blue':
        colorChoice = 'blue'
    elif color == 'purple':
        colorChoice = 'purple'
    else:
        print("Error - An unknown error has occured.")

elif animal == 'fish':
    animalChoice = 'fish'

    if color == 'red':
        colorChoice = 'red'
    elif color == 'blue':
        colorChoice = 'blue'
    elif color == 'purple':
        colorChoice = 'purple'
    else:
        print("Error - An unknown error has occured.")

if error:
    print("Error - Incorrect user input. Please check your spelling and try again.")
else:
    print(f"""The user chose: 
    Animal: {animalChoice}
    Color: {colorChoice}""")