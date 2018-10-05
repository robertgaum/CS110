#Counting using loops
for x in range(1,11):
    print(x)

print()

y = 1
while y < 11:
    print(y)
    y += 1

print()

#The unordered number list
numList = (3, 6, 1, 9, 15, 11, 13, 7, 2)

#Largest number in a list
largest = numList[0]

for number in numList:
    if number > largest:
        largest = number
else:
    print(f"The largest number is: {largest}")

print()

#Smallest number in a list
smallest = numList[0]

for number in numList:
    if number < smallest:
        smallest = number
else:
    print(f"The smallest number is: {smallest}")

print()

#Average of numbers in a list
counter = 0
total = 0

for number in numList:
    counter += 1
    total = total + number
else:
    print(f"The average is: {total/counter}")

print()