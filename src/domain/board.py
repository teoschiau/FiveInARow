import numpy as np

class Board:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__board = np.zeros((row, col))
        for r in range(row):
            for c in range(col):
                if r == 0:
                    self.set_coords(r, c, c)
                if c == 0:
                    self.set_coords(r, c, r)
    def pass_board(self):
        return self.__board
    def get_coords(self, x, y):
        return self.__board[x][y]
    def set_coords(self, x, y, new):
        self.__board[x][y] = new
    def add_stone(self, x, y, number):
        self.__board[x][y] = number

