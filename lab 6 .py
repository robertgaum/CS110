import random
def main():
    t = 0
    while t < 5:
        try:
            gamelis = userposition(hashtag)
        except IndexError:
            print('invalid input')
            continue
        gamerow = gamelis[0]
        t = t + 1
        gamecolumb = gamelis[1]
        game(gamerow, gamecolumb)
        if t is 5:
            break
        aiposition(hashtag)
        show(hashtag)
        gameover = end(hashtag)
        if gameover is 1:
            break
    show(hashtag)
    if t is 5:
        print('draw')
# asks user where to place x
def userposition(hashtag):
    gamerow = int(input('row:'))
    gamecolumb = int(input('columb:'))
    while hashtag[gamerow][gamecolumb] != ' ':
        print('spot is taken')
        gamerow = int(input('row:'))
        gamecolumb = int(input('columb:'))
    gamelis = (gamerow, gamecolumb)
    return gamelis
hashtag = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# places x in game
def game(gamerow, gamecolumb):
    for row in hashtag:
        for columb in row:
            hashtag[gamerow][gamecolumb] = 'X'
    return hashtag
# ai player selects random spot and places o at that spot
def aiposition(hashtag):
    airow = int(random.randrange(0, 3))
    aicolumb = int(random.randrange(0, 3))
    while hashtag[airow][aicolumb] != ' ':
        airow = int(random.randrange(0, 3))
        aicolumb = int(random.randrange(0, 3))
    hashtag[airow][aicolumb] = 'O'
    return hashtag
# prints the game
def show(hashtag):
    for row in hashtag:
        for columb in row:
            print(columb, end = ' ')
        print('')
# determines winner
def end(hashtag):
    gameover = ''
    x = 0
    y = 0
    while x != 3:
        if hashtag[x][y] == hashtag[x][y+1]:
            if hashtag[x][y] == hashtag[x][y+2]:
                if hashtag[x][y] == 'X':
                    print('you win')
                    gameover = 1
                elif hashtag[x][y] == 'O':
                    print('you loose')
                    gameover = 1
        x = x + 1
    while y != 3:
        x = 0
        if hashtag[x][y] == hashtag[x + 1][y]:
            if hashtag[x][y] == hashtag[x+2][y]:
                if hashtag[x][y] == 'X':
                    print('you win')
                    gameover = 1
                elif hashtag[x][y] == 'O':
                    print('you loose')
                    gameover = 1
        y = y + 1
    if hashtag[1][1] == hashtag [0][0]:
        if hashtag[1][1] == hashtag[2][2]:
            if hashtag[1][1] == 'X':
                print('you win')
                gameover = 1
            elif hashtag[1][1] == 'O':
                print('you loose')
                gameover = 1
    elif hashtag[1][1] == hashtag [0][2]:
        if hashtag[1][1] == hashtag[2][0]:
            if hashtag[1][1] == 'X':
                print('you win')
                gameover = 1
            elif hashtag[1][1] == 'O':
                print('you loose')
                gameover = 1
    return gameover
restart = ''
while restart != "no":
    hashtag = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    main()
    restart = input('wana play another round yes/no:')
