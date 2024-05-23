from random import choice
from Models.TicTacToeBoard import TicTacToeBoard
from Models.Player import Player
from time import sleep

class MachinePlayer(Player):
    def __init__(self, game_board: TicTacToeBoard):
        super().__init__(game_board)

    def play(self) -> bool:
        move: tuple = choice(self.game_board.empty_spots)
        sleep(1)
        return self._move(move)