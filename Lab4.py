#Stacks
selection = ""
stack = []

while (selection != "exit"):
    print("Select from the following options: 'Bold', 'Underline', 'Highlight', 'Undo'.")
    selection = input().lower()
    if selection == 'bold':
        stack.append('Bold')
        print("Bolded Text")
    elif selection == 'underline':
        stack.append('Underline')
        print("Underlined Text")
    elif selection == 'highlight':
        stack.append('Highlight')
        print("Highlighted Text")
    elif selection == 'undo':
        if len(stack) == 0:
            print("Nothing to undo!")
            continue
        else:
            print("Undo: "+ stack.pop())
    else:
        print("Error, incorrect input.")

#Queues
selection = ""
queue = []

while (selection != "exit"):
    print("Select from the following options: 'Enqueue', 'Dequeue', 'Print'.")
    selection = input().lower()
    if selection == 'enqueue':
        print("Enter name of person to queue: ")
        person = input()
        queue.append(person)
        print(f"Queued: {person}")
    elif selection == 'dequeue':
        print(f"{queue[0]} left the queue.")
        del queue[0]
    elif selection == 'print':
        print(queue)
    else:
        print("Error, incorrect input.")

#2D Lists
matrix = []

for row in range(0,4):
    #Create a new, blank row
    matrix.append([])
    for col in range(0,4):
        #Even
        if (row + col) % 2 == 0:
            matrix[row].append('X')
        #Odd
        if (row + col) % 2 != 0:
            matrix[row].append('O')

for index in range(0,4):
    print(matrix[index])    