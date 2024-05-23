from random import choice
from Models.TicTacToeBoard import TicTacToeBoard
from Models.Player import Player

class PersonPlayer(Player):
    def __init__(self, game_board: TicTacToeBoard):
        super().__init__(game_board)

    def __display_symbol(self):
        message = f'Your symbol: {self._symbol}'
        print(message)

    def __choose(self):
        self.__display_symbol()
        message = f'Press any key + enter to choose and just enter do deny.'
        print(message, 'Choose:', sep='\n')
        for spot in self.game_board.empty_spots:
            _spot = [str(x) for x in spot]
            choice = input(f"{','.join(_spot)}: ")
            if choice:
                return tuple(spot)
            
        self.game_board.display()
        return self.__choose()

    def play(self):
        move = self.__choose()
        return self._move(move)