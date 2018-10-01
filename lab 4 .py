# stack that asks user to input command or undue command then prints what user selected
stack = []
lis = ('bold','highlight','underline','undue','exit')
d = ""
while d != lis[4]:
    d = input('select bold, highlight, undue, underline, or exit').lower()
    if d == lis[0] or d == lis[1] or d == lis[2]:
        stack.append(d)
    elif d == lis[3]:
       pop = stack.pop()
       print(f'''you selected {stack} you undid {pop}''')
    else: break
# queue that gives option of dequeue, queue, or print queue, then asks for the name of the person
q = ''
queue = []
qlis = ('queue','de-queue','print queue')
while q != qlis[2]:
    q = input('select queue, de-queue, or print queue:').lower()
    if q == qlis[2]:
        break
    who = input(f'who would you like to {q}:')
    if q == qlis[0]:
        queue.append(who)
    elif q == qlis[1]:
        queue.remove(who)
print(queue)
# prints an array, couldn't get it to change characters to x and o
a = [[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]
for r in a:
    for c in r:
        print(c, end = ' ')
    print()