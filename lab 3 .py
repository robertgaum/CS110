import random
# for loop to print 1-10
for x in range(1,11):
    print(x)
y = 1
# while loop to print 1-10
while y <= 10:
    print(y)
    y += 1
# guessing game
lis = ('dog','cat','rock','car','cup')
ran = random.randrange(0,4)
sec = lis[ran]
inp = input(' guess a word from the list: dog, cat, rock, car, cup:').lower()
attempts = 1
# while loop for game
while inp is not sec:
    ran = random.randrange(0,4)
    sec = lis[ran]
    inp = input('nope guess again:').lower()
    attempts += 1
    if attempts == 3:
        print('you loose')   
        break
if sec is ran: print('you win')
# rock paper sissors game. Doesn't work, not sure how to fix it
rpslis = ('rock','paper','sissors','exit')
rpsran = random.randrange(0,2)
rpssec = rpslis[rpsran]
rpsinp = input('choose rock paper sissors or exit').lower()
while rpsinp != ('exit'):
    rpsran = random.randrange(0,2)
    rpssec = rpslis[rpsran]
    rpsinp = input('choose rock paper sissors or exit').lower()
    if rpssec is ('rock'):
        if rpsinp is ('paper'):
            print('rock, you win')
        if rpsinp is ('sissors'):
            print('rock, you loose')
    if rpssec is ('paper'):
        if rpsinp is ('rock'):
            print('paper, you loose')
        if rpsinp is ('sissors'):
            print('paper, you win')
    if rpssec is ('sissors'):
        if rpsinp is ('rock'):
            print('sissors, you win')
        if rpsinp is ('paper'):
            print('sissors, you loose')
    if rpssec is rpsinp:
        print('tie')
print('game over')