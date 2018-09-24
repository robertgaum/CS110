#I make a for loop that prints numbers 1 through 11.
for num in range(1,11):
    print (num)

#I make a while loop that prints numbers 1 through 11.
whileNum = 0
while whileNum <= 9:
    whileNum = whileNum + 1
    print (whileNum)

#I create a list of numbers and print the minimum, maximum and average of the values in the array.
numbers = (3,6,1,9,15,11,13,7,2)
biggest = numbers[0]
smallest = numbers[0]

for bigs in range(1,len(numbers)):
    if numbers[bigs] > biggest:
        biggest = numbers [bigs]
print(">> The max number is", biggest)

for smalls in range(1,len(numbers)):
    if numbers[smalls] < smallest:
        smallest = numbers [smalls]
print(">> The min number is", smallest)

average = 0
Sum = 0
for n in numbers:
    Sum = (Sum + n)
    average = Sum / len(numbers)

print (f">> The average number is: {average}")
