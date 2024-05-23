from random import choice
from Models.TicTacToeBoard import TicTacToeBoard
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, game_board: TicTacToeBoard):
        self.game_board = game_board
        self._symbol = None
        self.last_move = None

    @property
    def symbol(self) -> str:
        return self._symbol

    @symbol.setter
    def symbol(self, new_symbol) -> None:
        self._symbol = new_symbol

    @abstractmethod
    def play(self) -> bool:
        pass

    def _move(self, move) -> bool:
        is_possible = self.game_board.is_move_possible(*move)
        if not is_possible:
            return False

        self.game_board.make_move(*move, self._symbol)
        self.last_move = move
        return True
