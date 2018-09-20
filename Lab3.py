import random

for Number in range(0,10):
    Number = Number + 1
    print (Number)

Num = 0
while Num <= 10:
    Num = Num + 1
    print (Num)

List = ["Dog","Spider","Plant","House","Television"]
CorrectAnswer = random.randrange(0,4)
Answer = List[CorrectAnswer]
GuessNum = 0
while GuessNum < 3:
    print (">>Guess a thing out of this list:")
    print (f">>{List}")
    Guess = input()
    if Guess != List:
        GuessNum = GuessNum + 1
        print (">>Guess again.")
    
    if GuessNum >= 3:
        print (">>Too many attempts!")
        print ("Thank you for playing!")
        break

    if Guess in List:
        print (">>Congrats! You got it right!")
        print ("Thank you for playing!")
        break


ListRPS = ["Rock","Paper","Scissors"]
RandRPS = random.randrange(0,2)
CorrectRPS = List[RandRPS]

print (">>Rock, Paper, or Scissors?")
UserRPS = input()
while (CorrectRPS) = ("Rock"):
    print (CorrectRPS)

    if (UserRPS).title() = ("Paper"):
        print (">> You win!")
        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break

    if (UserRPS).title() = ("Rock"):
        print (">> Draw!")
        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break

    if (UserRPS).title() = ("Scissors"):
        print (">> You Lose!")
        print (">> Type 'Again' if you want to play again.")
        print (">> Type 'Exit' if you would like to stop playing.")
        Playagain = input().title()

        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()
        
        if Playagain = ("Exit"):
            break

while (CorrectRPS) = ("Scissors"):
    print (CorrectRPS)

    if (UserRPS).title() = ("Rock"):
        print (">> You win!")
        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break

    if (UserRPS).title() = ("Scissors"):
        print (">> Draw!")
        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break

    if (UserRPS).title() = ("Paper"):
        print (">> You Lose!")
        print (">> Type 'Again' if you want to play again.")
        print (">> Type 'Exit' if you would like to stop playing.")
        Playagain = input().title()

        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break

while (CorrectRPS) = ("Paper"):
    print (CorrectRPS)

    if (UserRPS).title() = ("Scissors"):
        print (">> You win!")
        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break

    if (UserRPS).title() = ("Paper"):
        print (">> Draw!")
        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break

    if (UserRPS).title() = ("Rock"):
        print (">> You Lose!")
        print (">> Type 'Again' if you want to play again.")
        print (">> Type 'Exit' if you would like to stop playing.")
        Playagain = input().title()

        if Playagain = ("Play Again"):
            print (">> Rock, Paper, or Scissors?")
            UserRPS = input()

        if Playagain = ("Exit"):
            print (">> Thank you for playing!")
            break