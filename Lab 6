import random

#Tic-Tac-Toe

#AI

class Board:
    def __init__(self):
        #Initialize an empty board
        self._board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    #Player is either X or O. Return true if successfull placement, else false.
    def PlaceToken(self, player, x, y):
        if self._board[x][y] == " ":
            self._board[x][y] = player
            return True
        else:
            return False


    #Player is the last player that played. Return true if win, else false.
    def Win(self, player, x, y):
        #check if previous move caused a win on vertical line 
        if self._board[0][y] == self._board[1][y] == self._board [2][y]:
            return True

        #check if previous move caused a win on horizontal line 
        elif self._board[x][0] == self._board[x][1] == self._board [x][2]:
            return True

        #check if previous move was on the main diagonal and caused a win
        elif x == y and self._board[0][0] == self._board[1][1] == self._board [2][2]:
            return True

        #check if previous move was on the secondary diagonal and caused a win
        elif x + y == 2 and self._board[0][2] == self._board[1][1] == self._board [2][0]:
            return True

        else:
            return False

    def printBoard(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                print(f" {self._board[i][j]} ", end='|')
            print('\n------------')

def main():
    newGame = Board()
    print("Welcome to Tic-Tac-Toe!")

    move = 1
    while move <= 9:
        #Player moves
        coords = input("Please enter where you would like to place your token: ")
        coords = coords.split(",")
        #Check whether that move is valid.
        try:
            if not newGame.PlaceToken("X", int(coords[0]), int(coords[1])):
                print("Invalid move.")
                newGame.printBoard()
                continue
        except:
            print("Invalid input format. The format is: x,y. With a range from 0-2")
            continue
        #Check for win
        if newGame.Win("X", int(coords[0]), int(coords[1])):
            print("You won!!!!")
            newGame.printBoard()
            break
        #AI moves
        #Check whether that move is valid and keep trying if not.
        valid = False
        while not valid:
            AIx = random.randint(0,2)
            AIy = random.randint(0,2)
            valid = newGame.PlaceToken("O", AIx, AIy)

        #Check for win
        if newGame.Win("O", AIx, AIy):
            print("You lost....")
            newGame.printBoard()
            break
        #Next move
        move = move + 1
        newGame.printBoard()
    else:
        print("That game was a draw!")
        newGame.printBoard()
    
if __name__ == '__main__': main()
