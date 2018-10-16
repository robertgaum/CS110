#_____________________________________________________________________
#                                                                     |
#                           L I S T S                                 |
#_____________________________________________________________________|

actionList = ["Treat","Toy","Blanket"]
yesnoList = ["Yes","No"]
moodList = ['Friendly','Playful','Sleepy']



#_____________________________________________________________________
#                                                                     |
#                         F U N C T I O N S                           |
#_____________________________________________________________________|

def inp(prompt):
    print("")
    global Inp
    Inp = input(prompt).title()


def __yesno__(self):
    n = 0
    global yesno
    yesno = input(">> Would you like to give it something? (Yes or No) ").title()
    print("")
    print(f">> YOU ENTERED: {yesno}")
    if n > 1:
        yesno = input(f">> Would you like to give the {Dog.breed} another item?: (YES OR NO)").title()


def __actionMenu__(self):
    print(" ________________________")
    print("|                        |")
    print("|       PICK ONE:        |")
    print("|                        |")
    print("| TREAT | TOY | BLANKET  |")
    print("|________________________|")
    print("")
    global action
    action = input(">> ENTER HERE: ").title()
    print("")
    print (f">> YOU ENTERED: {action}")
    print("")



#_____________________________________________________________________
#                                                                     |
#                         C L A S S E S                               |
#_____________________________________________________________________|

class Dog:
    
    def __init__(self, **kwargs):
        self._breed = kwargs['breed']
        self._mood = kwargs['mood']
        self._color = kwargs['color']

    def breed(self, myBreed = None):
        if myBreed:
            self._breed = myBreed
            return self._breed
    
    def color(self, myColor = None):
        if myColor:
            self._color = myColor
            return myColor

    def give(self, myMood = None):
        if myMood:
            self._mood = myMood

        if action == "Treat":
            myMood == "Friendly"
            return myMood
        
        if action == "Toy":
            myMood == "Playful"
            return myMood
                
        if action == "Blanket":
            myMood == "Sleepy"
            return myMood

def __str__(self):
    string = f"Your {self._mood} {self._breed} is {self._color}."
    if string:
        self._string = string
        return string

def main():
    myDog = Dog(breed = "chihuahua" , mood = "Playful" , color = "Brown")
    print("")
    print (__str__(myDog))
    print("")
    __yesno__(None)

    while yesno == ("Yes"):
        
        print("")
        print(">> Here's a list:")
        __actionMenu__(None)

        if action in actionList:
            if action == actionList[0]:
                Dog.give("Treat")
                print("")
                print (__str__(myDog))
                print("")

            if action == actionList[1]:
                Dog.give("Toy")
                print("")
                print (__str__(myDog))
                print("")

            if action == actionList[2]:
                Dog.give("Blanket")
                print("")
                print (__str__(myDog))
                print("")


        while action not in actionList:
            print("")
            print (">> INVALID ACTION! TRY AGAIN: ")
            __actionMenu__(None)

    if yesno == ("No"):
        print(">> GOODBYE!")
        exit

    else:
        print(">> THIS IS NOT A VALID ANSWER!")
        __yesno__(None)

if __name__ == "__main__":
    main()
