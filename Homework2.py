#Hello, welcome to my program!

#First, I define the variables for the dictionary as the user inputs.
Profile_FirstName = input('Please enter your first name: ')
Profile_LastName = input('Please enter your last name: ')
Profile_Age = input('Please enter your Current Age: ')
Profile_FirstNumber = input('Please enter a number: ')
Profile_SecondNumber = input('Please enter another number: ')

#Then, I define the dictionary known as 'Profile'
Profile = {
    'FirstName':'FirstName', 
    'LastName':'LastName', 
    'Age':'Age', 
    'FirstNumber':'FirstNumber', 
    'SecondNumber':'SecondNumber' 
    }

#Next, I define the values of the keys in the dictionary 
# as the previously mentioned user input variables.
Profile['FirstName'] = Profile_FirstName
Profile['LastName'] = Profile_LastName
Profile['Age'] = Profile_Age
Profile['FirstNumber'] = Profile_FirstNumber
Profile['SecondNumber'] = Profile_SecondNumber

#Then, I print the dictionary with the user's data plugged in.
print (Profile)

print (type(Profile['Age']))

#Next, I print out a sentence that has the user's specified first and last name.
print (f'Hello, {Profile_FirstName} {Profile_LastName}! Nice weather today, no?')

#Lastly, I print out the result of the Profile_FirstNumber to the power of Profile_SecondNumber
print (int(Profile_FirstNumber)^int(Profile_SecondNumber)) 

print ('Python is an object-oriented programming language.An object is anything that has an identity, type, and a value. In other words, everything in python is an object.')
