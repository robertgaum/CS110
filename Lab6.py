import random
from abc import ABC, abstractmethod
from enum import Enum


class NotEmptyError(Exception):
    pass


class Token(Enum):
    EMPTY = " "
    PLAYER1 = "X"
    PLAYER2 = "O"


class Board:
    availableSlots = 9

    State = [[Token.EMPTY, Token.EMPTY, Token.EMPTY],
             [Token.EMPTY, Token.EMPTY, Token.EMPTY],
             [Token.EMPTY, Token.EMPTY, Token.EMPTY]]


    def PrintMap(self):
        print("")
        print("       ||       ||      ")
        print(f"   {self.State[0][0].value}   ||   {self.State[0][1].value}   ||   {self.State[0][2].value}  ")
        print("       ||       ||      ")
        print("=======||=======||=======")
        print("       ||       ||       ")
        print(f"   {self.State[1][0].value}   ||   {self.State[1][1].value}   ||   {self.State[1][2].value}  ")
        print("       ||       ||       ")
        print("=======||=======||=======")
        print("       ||       ||      ")
        print(f"   {self.State[2][0].value}   ||   {self.State[2][1].value}   ||   {self.State[2][2].value}  ")
        print("       ||       ||      ")
        print("")

    def PrintMapNum(self):
        print(Token.EMPTY.value)
        print("HERE IS THE MAP:")
        print("")
        print("         ||         ||         ")
        print("   0,0   ||   0,1   ||   0,2   ")
        print("         ||         ||         ")
        print("=========||=========||=========")
        print("         ||         ||         ")
        print("   1,0   ||   1,1   ||   1,2   ")
        print("         ||         ||         ")
        print("=========||=========||=========")
        print("         ||         ||         ")
        print("   2,0   ||   2,1   ||   2,2   ")
        print("         ||         ||         ")
        print(Token.EMPTY.value)

    def place(self, token, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise IndexError("This is not a valid place")
        if self.State[x][y] != Token.EMPTY:
            raise NotEmptyError("There already is a token in this spot.")
        self.State[x][y] = token
        self.availableSlots = self.availableSlots - 1

    def check_victory(self, x, y):
        if self.State[0][y] == self.State[1][y] == self.State[2][y]:
            return True, self.State[0][y]

        if self.State[x][0] == self.State[x][1] == self.State[x][2]:
            return True, self.State[x][0]

        if x == y and self.State[0][0] == self.State[1][1] == self.State[2][2]:
            return True, self.State[0][0]

        if x + y == 2 and self.State[0][2] == self.State[1][1] == self.State[2][0]:
            return True, self.State[0][2]

        if self.availableSlots == 0:
            return True, Token.EMPTY

        return False, None


class Actor(ABC):
    @abstractmethod
    def get_move(self):
        pass


class PersonActor(Actor):

    def get_move(self):
        board.PrintMapNum()
        player_input = input("Please enter the coordinates as (x,y): ")
        while not self.is_valid_input(player_input):
            player_input = input("Please enter valid coordinates as (x,y): ")
        return map(int, player_input.split(","))

    @staticmethod
    def is_valid_input(player_input):
        if len(player_input.split(",")) != 2:
            return False
        try:
            map(int, player_input.split(","))
        except ValueError:
            return False
        return True


class RandomActor(Actor):

    def get_move(self):
        return random.randint(0, 2), random.randint(0, 2)


class Game:
    turn = 0
    winner = None

    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def next_turn(self):
        if self.turn % 2 == 0:
            print(Token.EMPTY.value)
            print("Player 1's turn")
            self.take_turn(self.player1, Token.PLAYER1)
        else:
            print("Player 2's turn")
            self.take_turn(self.player2, Token.PLAYER2)
        self.board.PrintMap()

    def take_turn(self, player, token):
        unsuccessful_move = True
        while unsuccessful_move:
            x, y = player.get_move()
            try:
                self.board.place(token, x, y)
                _, self.winner = self.board.check_victory(x, y)
                unsuccessful_move = False
                self.turn = self.turn + 1
            except (NotEmptyError, IndexError) as e:
                print(e)
                pass

    def play(self):
        while self.winner is None:
            self.next_turn()


if __name__ == '__main__':
    player1 = PersonActor()
    player2 = RandomActor()
    board = Board()
    game = Game(board, player1, player2)
    game.play()
    print(f"Winner: {game.winner}")