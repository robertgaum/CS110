#Get the users first name, last name, age.
print('Enter your first name: ')
firstName = input()

print('Enter your last name: ')
lastName = input()

print('Enter your age: ')
age = input()

#Print out the user information gathered above.
print(f'Hello, {firstName} {lastName}, you are {age} years old.')

#Get two numbers from the user.
print('Pick the first number to multiply: ')
firstNum = input()

print('Pick the second number to multiply: ')
secondNum = input()

product = int(firstNum) * int(secondNum)

#Print out product of the two numbers gathered above.
print(product)