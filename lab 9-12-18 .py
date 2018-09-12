# set values and calculated type
x = 2
y = '2'
z = True
if type(x) is int:
    print('is an integer')
if type(y) is str:
    print ('is a string')
if type(z) is bool:
    print('is a boolien value')   
# answered questions
print ('''a is false
b is false
c is true
d is false
e is true''')
# created two lists and asked user to choose from them
a = ['dog', 'cat', 'starnose mole', 'rock', 'tiger']
c = ['pink', 'green', 'blue', 'black', 'purple', 'red']
animal = input('''Please choose your favorite anamal from the 
following list:
dog, cat, starnose mole, rock, and tiger:''' ).lower()
color = input('''please choose your favorite color from the
following list:
pink, green, blue, black, purple, and red:''').lower()
# made if statement so that user must choose from the lists
if (animal in a) and (color in c):
 print (f'''Your favorite color is {color} and 
 your favorite animal is {animal}.''')
else: 
    print('you need to choose from the lists')