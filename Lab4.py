List = []
Type = ["Stack","Queue","Array"]
print ("| Stack | Queue | Array |")
print (">> Choose one:")

choice = input().title()

while choice in Type:

    if choice == Type[0]:

        print ("| Bold | Highlight | Underline | Undo |")
        print (List)
        Actionlist = ["Bold", "Highlight", "Underline", "Undo"]
        action = input().title()
            
        while action in Actionlist:

            if action != (Actionlist[3]):
                List.append(action)
                print (f">> You selected {action}")
                print("")
                print (List)
                print ("")
                print ("| Bold | Highlight | Underline | Undo |")
                action = input().title()
                
            if action == (Actionlist[3]):
                List.pop()
                print (f">> You selected {action}.")
                print ("")
                print (List)
                print ("")
                print ("| Bold | Highlight | Underline | Undo |")
                action = input().title()
                        
            while len(Actionlist) == 0:
                print (">> There are no actions to undo.")
                print (">> Please enter another action.")
                print ("")
                print ("| Bold | Highlight | Underline | Undo |")
                action = input().title()

            if action.title() not in Actionlist:
                print (f">> You selected {action}")
                print ("")
                print (List)
                print ("")
                print ("REEEEEEEEE")
                print (">> This is not a valid input. Please try again.")
                print ("| Bold | Highlight | Underline | Undo |")
                action = input().title()

            print ("")
            print (List)
            print ("")
            print (">> Would you like to continue?1")
            print (">> Type YES or NO")        
            playagain = input()

            if playagain.title() == ("No"):
                print ("Goodbye")
                break

    if choice == Type[1]:
        queue = []
        queueactionList = ["Add","Remove","Exit"]
        print ("| ADD TO QUEUE | REMOVE FROM QUEUE | EXIT |")
        queueaction = input().title()

        while queueaction in queueactionList:
            
            if queueaction == queueactionList[0]:
                print ("")
                print (">> What would you like to place in the queue?")
                print ("| ENTER A STRING, INTEGER, OR BOOLEAN")
                Qadd = input()
                print (">> What place do you want your input to be in the queue?")
                print ("")
                print (">> Enter a number:")
                Qaddplace = int(input())
                queue.insert(Qaddplace,Qadd)
                print (queue)
                print ("")
                print ("| ADD TO QUEUE | REMOVE FROM QUEUE | EXIT |")
                print ("")
                queueaction = input().title()
                

            if queueaction == queueactionList[1]:
                print ("")
                print (">> What place do you want your input to be in the queue?")
                print ("")
                print (">> Enter a number:")
                Qremoveplace = int(input())
                queue.pop(Qremoveplace)

                print (queue)
                print ("")
                print ("| ADD TO QUEUE | REMOVE FROM QUEUE | EXIT |")
                print ("")
                queueaction = input().title()
            
            if queueaction == queueactionList[2]:
                print (">> You have entered EXIT")
                print (">> GOODBYE")
                break

    if choice == Type[2]:
        matric = []
        for row in range(0,3):
            for column in range(0,3):

                if (row + column) % 2:
                    matric.append("O")

                else:
                    matric.append("X")