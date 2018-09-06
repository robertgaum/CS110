myDictionary = {'firstName': input('Enter your first name: '), 
                'lastName': input('Enter your last name: '), 
                'age': input('Enter your age: '),
                'firstNumber': input('Choose a number: '), 
                'secondNumber': input('Choose another number: ')}

print (myDictionary)

x = myDictionary['age']

print (type(x))
print ('Hello', myDictionary['firstName'], myDictionary['lastName'],', welcome to my program!')

x = int(myDictionary['firstNumber'])
y = int(myDictionary['secondNumber'])

print (x**y)

print ('''Everything in Python is an Object. Objects have attributes (properties) and methods (actions).
Attributes describe the object, while methods perform an action within that object.''')