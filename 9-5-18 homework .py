# created a dictionary and asked user to input the keys 
mydictionary = {'firstname': input('what is your first name?'), 
'lastname': input('what is you last name?'), 'age': input('what is yout age?'),
'firstnumber': input('enter a number'), 'secondnumber': 
input('enter another number')}
#printed dictionaty, type for age, and a sentace with key values
print (mydictionary)
x = mydictionary['age']
print (type(x))
print ('hello', mydictionary['firstname'], mydictionary['lastname'],'how are you?')
#take a value from the dictionary to the power of another
x = int(mydictionary['firstnumber'])
y = int(mydictionary['secondnumber'])
z = x**y
print ('{0} to the power of {1} is {2}'.format(x,y,z))
# I defined what an object is.
print ('''An object in python is a veriable that has uniqe attributes and methods 
that can be preformed with it. For example, the first number that you intered 
had the attribute of a value and was abel to be changed useing a mathamatical
 method. ''') 
