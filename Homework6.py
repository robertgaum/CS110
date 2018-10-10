#L I S T S

YesnoList = ["Yes", "No",]


#F U N C T I O N S

def getInput(question):
    print (question)
    Input = input()
    print (f"You entered {Input}")
    return Input

def isPrime(number):
    print("")
    print (number)
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            print(">> NOT PRIME")
            return False
    else:
        print(">> PRIME")        
    return True

def isEven(number):
    if number % 2 == 0:
        print("")
        print (">> NUMBER IS EVEN")
        print("")
        return True
    else:
        print("")
        print (">> NUMBER IS ODD")
        print("")
        return False

def printPrime(bool1):
    bool1 = bool(input(">> PLEASE ENTER A BOOLEAN VALUE: ").title())
    print(f"You entered {bool1}")
    if bool1 == True:
        print(">> PRIME")
        print("")
        return True

    if bool1 == False:
        print(">> NOT PRIME")
        print("")
        return False

def printEven(bool2):
    bool2 = bool(input(">> PLEASE ENTER A BOOLEAN VALUE: ").title())
    print(f"You entered {bool2}")
    if bool2 == True:
        print(">> PRIME")
        print("")
        return True

    if bool2 == False:
        print(">> NOT PRIME")
        print("")
        return False

def cont(function):
    print(">> WOULD YOU LIKE TO CONTINUE?")
    yesno = input().title()
    
    if yesno == (YesnoList[0]):
        return True
    else:
        return False   



def main():
    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("|                                         |") 
    print("|  Please pick the corresponding number   |")
    print("|   for the function you wish to run.     |")
    print("|                                         |")
    print("|     (1) getInput                        |")
    print("|     (2) isPrime                         |")
    print("|     (3) isEven                          |")
    print("|     (4) printPrime                      |")
    print("|     (5) printEven                       |")
    print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
    print(" ")
    
    choice = int(input(">> INPUT NUMBER: "))
    print (choice)

    if choice < 6:

        if choice == 1:
            #GetInput
            Input = getInput(">> Enter anything")

        if choice == 2:
            #isPrime
            n = int(input(">> ENTER ANOTHER NUMBER: "))
            isPrime(n)

        if choice == 3:
            Input = int(input(">> ENTER A NUMBER: "))
            isEven(Input)

        if choice == 4:
            Bool = input(">> ENTER A BOOLEAN VALUE: ")
            printPrime(Bool)
            
        if choice == 5:
            Boool = bool(input(">> ENTER A BOOLEAN VALUE: "))
            printEven(boool)


if __name__ == "__main__":
    main()