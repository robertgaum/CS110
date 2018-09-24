# used a for look to print 1-10
i = +1
for i in range(1,11):
    print(i)
y = 1
# while loop to print 1-10
while y < 11:
    print(y)
    y = y + 1
# set objects to use for next loop
lis = (3,6,9,15,1,11,13,7,2)
a = lis[0]
b = lis[1]
c = lis[0]
d = lis[1]
trys = 0
tot = 0
# used while loop to find largest num, smallest num, and average
while trys != 9:
    # this branch is for smallest num
    if a > b:
        # this is for the largest
        a = lis[+ trys]
        if c < d:
            c = lis[+ trys]
        else: d = lis[+ trys]
    else:
        # also for the largest
        b = lis[+ trys]
        if c < d:
            c = lis[+ trys]
        else: d = lis[+ trys]
    # this is for the average
    tot = tot + lis[+ trys]
    trys = trys + 1
ave = tot / trys
print(f'''{b} is the smallent number in the list.
{c} is the largest number in the list
the average is {ave}''')
