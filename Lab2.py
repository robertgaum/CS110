#First, I set the variable of 'x' equal to 2
x = 2

#Second, I set the variable of 'y' equal to "2"
y = "2"

#third, I set the variable of 'z' equal to True
z = True

#Next, I create a conditional statement that calculates the type of the above variables and prints out the type. 
print(type(x))
print(type(y))
print(type(z))

#Next, I print the followint statements' answers
print (True or True and False)
print ((True and False) and (True or False) or (False and False))
print (5 >= 5 and 2 is 2)
print (2 in [1,3,5,7,9])
print (7 > 3 + 3)

#Next, I ask the user about their favorite animal from a list of animals
UserAnimal = input(">>Please enter the name of your favorite animal: ")
print (f">>Your answer was: {UserAnimal}")

AnimalList = ["Dog", "Cat", "Bird", "Fish", "Snake", "Rock"]
ColorList = ["Red","Blue","Green","Yellow","Purple"]

while ((UserAnimal).title() not in (AnimalList)):
    print (">>Wrong Animal! *Sad music plays*")
    UserAnimal = (input(">>Please enter a different animal:"))
    
if ((UserAnimal).title() in (AnimalList)):
    print (">>YAY! Your answer was on the list!")
    UserColor = input(">>Please enter a color:")
    print (f">>Your answer was: {UserColor}")
    print ("Your answer was on the list! YAY! *'We are the champions by queen' plays*")
    
    while ((UserColor).title() not in (ColorList)):
        print(f">>Your answer was: {UserColor}.")
        print(">>Wrong Color! *Sad music plays*")
        UserColor = (input(">>Please enter a different color: "))
        
        if ((UserColor).title() in (ColorList)):
            print (f">>Your answers were {UserAnimal} and {UserColor}!")
            print (">>YAY!! *'We are the Champions' by Queen plays*")
            print (">>You picked the correct answers!")
