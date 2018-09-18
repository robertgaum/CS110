# ask user for type and value 
x = input('''Do you want to enter an integer, string, or 
boolean value:''').lower()
w = input(f'please enter the {x}:')
# list of types
z = ['integer','string','boolean']
# list of posible string values
y = ['dog', 'cat', 'fox', 'tiger', 'fish']
# if integer is greater, less, or equal to 5
if x in z[0]:
    if int(w) > 5: print(f'{w} is greater than five')
    elif int(w) < 5: print(f'{w} is less than five')
    elif int(w) == 5: print(f'{w} is equal to five')
# if string is in the list
elif x in z[1]:
    if type(w) is not str: print('input not valid')
    elif (w).lower() in y: print(f'{w} is in the list')
    elif (w).lower() not in y: print(f'{w} is not in the list')
 # answers questions related to bool
elif x in z[2]: 
    if w in 'true': print(True and True,(True and True)or False,True and False)
    elif w in 'false': print(False and True,(False and True)or False,False and False)
    else: print('input not valid')
# makes sure the first question is answered correctly
elif x not in z:print ('input not valid')