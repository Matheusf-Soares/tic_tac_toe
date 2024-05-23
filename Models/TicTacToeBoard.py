import pandas as pd
import numpy as np
import os
from time import sleep
from random import choice

class TicTacToeBoard:
    def __init__(self):
        self.__colunas = ['A', 'B', 'C']
        self.__index = [i for i in range(1, 4)]
        self.__move_count = int(0)
        self.__empty_spot_symbol = '⊡'
        
        self.symbols = ['✕', '◯']
        self.board = pd.DataFrame(columns=self.__colunas, index=self.__index).fillna(self.__empty_spot_symbol)
        self.winner_exists = False
        self.winner = None

    @property
    def empty_spots(self) -> list[tuple]:
        return self.__get_empty_spots()

    def get_symbol(self):
        symbol_chosen = choice (self.symbols)
        return symbol_chosen

    def display(self):
        os.system('clear')
        print(self.board)

    def __get_empty_spots(self):
        empty_spots = []
        for col in self.__colunas:
            for ind in self.__index:
                if self.board.loc[ind, col] == self.__empty_spot_symbol:
                    empty_spots.append((col, ind))
        
        return empty_spots

    def is_move_possible(self, column, index):
        if (column, index) not in self.empty_spots:
            return False
        return True

    def __find_winner(self):
        winner = [symbol for symbol in self.symbols if self.__is_winner(symbol)]
        if len(winner) > 0:
            self.winner_exists = True
            self.winner = winner[0]

    def __all_equal(line, symbol):
        line = np.array(line)
        return (line == symbol).all()

    def __is_winner(self, symbol):
        nd_board = np.array(self.board)
        diagonal_1 = (np.diagonal(nd_board) == symbol).all()
        diagonal_2 = (np.diagonal(np.fliplr(nd_board)) == symbol).all()

        lines = np.apply_along_axis(TicTacToeBoard.__all_equal, 1, nd_board, symbol=symbol).any()
        columns = np.apply_along_axis(TicTacToeBoard.__all_equal, 0, nd_board, symbol=symbol).any()

        is_winner = diagonal_1 or diagonal_2 or lines or columns 
        return is_winner

    def make_move(self, column, index, symbol ):
        self.board.loc[index, column] = symbol

        self.__move_count += 1
        if self.__move_count >= 5:
            self.__find_winner()