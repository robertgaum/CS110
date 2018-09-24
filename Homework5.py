#I make a for loop that prints numbers 1 through 11.
for num in range(1,11):
    print (num)

#I make a while loop that prints numbers 1 through 11.
whileNum = 0
while whileNum <= 9:
    whileNum = whileNum + 1
    print (whileNum)

#I create a list of numbers and print the minimum, maximum and average of the values in the array.
List = (3,6,1,9,15,11,13,7,2)
Max_value = max(List)
Min_value = min(List)
avg_value = sum(List)/len(List)

print (f">> Your maximum Value is: {Max_value}")
print (f">> Your minimum Value is: {Min_value}")
print (f">> Your average Value is: {avg_value}")
