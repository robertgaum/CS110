import random

for x in range(1,11):
    print(x)

y = 1
while y < 11:
    print(y)
    y += 1

#WORDGUESS
wordList = ('dog', 'cat', 'fish', 'bird', 'rabbit')
print("Guess the sectet animal from the following list: ")
print(wordList)
userWord = input()
randNum = random.randrange(0,5)
randWord = wordList[randNum]
attempts = 1
maxAttempts = 3

while randWord != userWord:
    if attempts >= maxAttempts:
        print('Too many attempts.')
        break
    print('Incorrect, try again.')
    userWord = input()
    attempts += 1
else:
    print('Correct! You guessed the secret animal!')

#ROCK PAPER SCISSORS
gameList = ('rock', 'paper', 'scissors', 'exit')
randNum = random.randrange(0,3)
randGame = gameList[randNum]
print('Choose between the following options: ')
print(gameList)
userChoice = input()

while userChoice != 'exit':
    if userChoice == 'rock':
        if randGame == 'rock':
            print('rock vs rock - Draw')
        elif randGame == 'paper':
            print('rock vs paper - Lose')
        elif randGame == 'scissors':
            print('rock vs scissors - Win')
    elif userChoice == 'paper':
        if randGame == 'rock':
            print('paper vs rock - Win')
        elif randGame == 'paper':
            print('paper vs paper - Draw')
        elif randGame == 'scissors':
            print('paper vs scissors - Lose')
    elif userChoice == 'scissors':
        if randGame == 'rock':
            print('scissors vs rock - Lose')
        elif randGame == 'paper':
            print('scissors vs paper - Win')
        elif randGame == 'scissors':
            print('scissors vs scissors - Draw')
    
    print('Choose between the following options: ')
    print(gameList)
    userChoice = input()
    randNum = random.randrange(0,3)
    randGame = gameList[randNum]

else:
    print("Bye! Thanks for playing!")

#PRIME
print("Enter any positive number to see whether it is prime: ")
prime = int(input())
for z in range(2, prime):
    if prime == 1:
        print("Not prime!")
        break
    if prime % z == 0:
        print("Not prime!")
        break
else:
    print("That is a prime!")