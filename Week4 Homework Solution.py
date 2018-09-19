print("Please enter: integer, string, or boolean...")
choice = input()

if choice == 'integer':
    print("Enter an integer value:")
    intChoice = int(input())

    if(intChoice > 5):
        print("Your selection is greater than 5.")
    elif(intChoice == 5):
        print("Your selection is equal to 5.")
    elif(intChoice < 5):
        print("Your selection is less than 5.")
    else:
        print("Error - Incorrect input.")

elif choice == 'string':
    print("Enter a string value:")
    strChoice = input().lower()
    myList = ("dog", "cat", "fox", "tiger", "fish")

    if strChoice in myList:
        print("You chose a nice animal!")
    else:
        print("Your animal is not in the list.")

elif choice == 'boolean':
    print("Enter a boolean value:")
    boolChoice = input().lower()

    if boolChoice == 'true':
        myBool = True
    elif boolChoice == 'false':
        myBool = False
    else:
        print("Error - Incorrect input.")

    print(myBool and True)
    print((myBool and True) or False)
    print(myBool or False)

else:
    print("Error - Enter only integer, string, or boolean.")