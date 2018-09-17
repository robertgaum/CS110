#First, I define the dictionary
Dict = ["Integer", "String", "Boolean","Int","Str","Bool"]

#Next, I prompt the user to enter their pick out of the three options
print (">> Please pick one option out of these three: ")
print (">> Integer, String, Or Boolean")

Answer = input().title()

#This is a loop to continue prompting the user if they do not enter a valid answer.
while (Answer).title() not in (Dict):
    print (">> Sorry, That answer was not valid")
    print (">> Please pick one option out of these three: ")
    print (">> Integer, String, Or Boolean")
    Answer = input()



#Next, I make a statement that if the answer is any of the options, to state that they picked they choose.

#This is the integer portion of the code.
if (Answer).title() == ("Integer"):
    print (">> Your answer was: Integer ")

    # Then, I prompt the user to choose an integer.
    print (">> Which integer do you choose?: ")
    UserInt = int(input())

    if (UserInt > 5):
        print (">> Your number is greater than 5")
    
    if (UserInt <= 5):
        print (">> Your number is less than 5")

#This is the string portion of the code.
if (Answer).title() == ("String"):
    print (">> Your answer was: String")
    Animals = ["Dog","Cat","Fox","Tiger","Fish"]
    print (">> Please enter an animal: ")

    #I made a list of Animals and defined a variable that is the input of the user.
    UserString = (input())
    # I wrote a conditional that states if the user answers an animal that is in the list, it will tell them.
    if (UserString).title in (Animals):
        # Not sure why this doesn't work.
        print (f">> Your Animal was {UserString}")
        print (">> Congrats! Your animal was on the list!")

    if (UserString).title() not in (Animals) :
        print (">> This is not an animal on the list! Try again.")
        print (">> Please enter a different animal:")
        UserString = input().title()

        

#This is the Boolean portion of the code.

if (Answer).title() == ("Boolean"):

    # I print out their input
    print (">> Your answer was: Boolean")

    # Then, I prompt the user to enter a Boolean value and use the value to define a variable
    print (">> Please enter a Boolean value (True or False): ")
    UserInput = (input())
    Bool = ["True", "False"]

    # Then, I print the value
    print (f">> Your value was '{UserInput}'")


    if (UserInput) in (Bool):
        UserBool = bool(UserInput)
        a = ((UserBool) and True)
        b = (((UserBool) and True) or False)
        c = ((UserBool) or False)
        print (a)
        print (b)
        print (c)
    
    if (UserInput) not in (Bool):
        print (">> Your input is not a boolean value. Please try again.")