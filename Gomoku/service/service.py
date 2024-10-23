import random

from src.domain.board import *

class Gameservice:
    def __init__(self, r, c):
        self.__board = Board(r, c)
    def pass_board(self):
        return self.__board.pass_board()
    def validate_placement(self, x, y):
        """
        function that validates the row and column inputed by the user
        :param x: row
        :param y: column
        :return: -
        """
        errors = ""
        if self.__board.get_coords(x, y) == 1 or self.__board.get_coords(x,y) == 2:
            errors += "The place is already occupied!"
        if x >= 21 or y >= 21:
            errors += "The place on the board doesn't exist!"
        if len(errors)!=0:
            raise Exception(errors)

    def validate_place(self, x, y):
        """
        function that returns 1 if there already is a stone on the place
        :param x: row
        :param y: column
        :return: returns 1 if there already is a stone on the place and 0 instead
        """
        ok = 0
        if self.__board.get_coords(x, y) == 1 or self.__board.get_coords(x, y) == 2:
            ok = 1
        return ok
    def add_stone(self, x, y, number):
        """
        function that adds a stone on the board
        :param x: row
        :param y: column
        :param number: the stone
        :return: -
        """
        self.validate_placement(x, y)
        self.__board.add_stone(x, y, number)

    def add_stone_ai(self, rows, cols, number, p2):
        """
        function that make the ai add a stone on the board
        :param rows: number of rows
        :param cols: number of columns
        :param number: the stone that the other player has
        :param p2: the stone that the ai has
        :return: -
        """
        ok = 1
        x = 0
        y = 0
        while ok == 1:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            ok = self.validate_place(x, y)
        if self.check_4(rows, cols, number, p2) == 0:
            self.__board.add_stone(x, y, p2)
    def check_win(self, rows, columns, piece):
        """
        function that checks if the there is a potential win
        :param rows: number of rows
        :param columns: number of cols
        :param piece: the stone specified
        :return: 0 if there is a piece, 1 if there is not
        """
        ok=0
        for r in range(rows):
            for c in range(columns-4):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r, c+1) == piece and self.__board.get_coords(r, c+2) == piece and self.__board.get_coords(r, c+3) == piece and self.__board.get_coords(r, c+4) == piece:
                    ok=1
        for r in range(rows-4):
            for c in range(columns):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r+1, c) == piece and self.__board.get_coords(r+2, c) == piece and self.__board.get_coords(r+3, c) == piece and self.__board.get_coords(r+4, c) == piece:
                    ok=1
        for r in range(rows - 4):
            for c in range(columns - 4):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1, c+1) == piece and self.__board.get_coords(r + 2, c+2) == piece and self.__board.get_coords(r + 3, c+3) == piece and self.__board.get_coords(r + 4, c+4) == piece:
                    ok = 1
        for r in range(rows-4):
            for c in range(4, columns):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1, c-1) == piece and self.__board.get_coords(r + 2, c-2) == piece and self.__board.get_coords(r + 3, c-3) == piece and self.__board.get_coords(r + 4, c-4) == piece:
                    ok = 1
        return ok
    def check_6(self, rows, columns, piece):
        """
        function that checks if there is an overline
        :param rows: number of rows
        :param columns: number of cols
        :param piece: the stone specified
        :return: 0 if there is not, 1 if there is an overline
        """
        ok = 0
        for r in range(rows):
            for c in range(columns - 5):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r,c + 1) == piece and self.__board.get_coords(r, c + 2) == piece and self.__board.get_coords(r, c + 3) == piece and self.__board.get_coords(r,c + 4) == piece and  self.__board.get_coords(r,c + 5) == piece:
                    ok = 1
        for r in range(rows - 5):
            for c in range(columns):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1,
                                                                                      c) == piece and self.__board.get_coords(
                        r + 2, c) == piece and self.__board.get_coords(r + 3, c) == piece and self.__board.get_coords(r + 4, c) == piece and self.__board.get_coords(r + 5, c) == piece:
                    ok = 1
        for r in range(rows - 5):
            for c in range(columns - 5):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1,
                                                                                      c + 1) == piece and self.__board.get_coords(
                        r + 2, c + 2) == piece and self.__board.get_coords(r + 3,
                                                                           c + 3) == piece and self.__board.get_coords(r + 4, c + 4) == piece and self.__board.get_coords(r + 5, c + 5) == piece:
                    ok = 1
        for r in range(rows-5):
            for c in range(5, columns):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1,
                                                                                      c - 1) == piece and self.__board.get_coords(
                        r + 2, c - 2) == piece and self.__board.get_coords(r + 3,
                                                                           c - 3) == piece and self.__board.get_coords(r + 4, c - 4) == piece and self.__board.get_coords(r + 5, c - 5) == piece:
                    ok = 1
        return ok
    def check_4(self, rows, columns, piece, p2 ):
        """
        function that checks if thee is almost a win for the ai to try and stop the player from winning
        :param rows:numbers of rows
        :param columns: numbers of cols
        :param piece: the player's stone
        :param p2: the ai's stone
        :return:
        """
        ok = 0
        for r in range(rows):
            for c in range(columns - 3):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r,
                                                                                      c + 1) == piece and self.__board.get_coords(
                        r, c + 2) == piece and self.__board.get_coords(r, c + 3) == piece:
                    ok = 1
                    self.__board.set_coords(r, c + 4, p2)
        for r in range(rows - 3):
            for c in range(columns):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1,
                                                                                      c) == piece and self.__board.get_coords(
                        r + 2, c) == piece and self.__board.get_coords(r + 3, c) == piece:
                    ok = 1
                    self.__board.set_coords(r+4, c, p2)
        for r in range(rows - 3):
            for c in range(columns - 3):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1,
                                                                                      c + 1) == piece and self.__board.get_coords(
                        r + 2, c + 2) == piece and self.__board.get_coords(r + 3,c + 3) == piece:

                    ok = 1
                    self.__board.set_coords(r + 4, c + 4, p2)
        for r in range(rows - 3):
            for c in range(3, columns):
                if self.__board.get_coords(r, c) == piece and self.__board.get_coords(r + 1,
                                                                                      c - 1) == piece and self.__board.get_coords(
                        r + 2, c - 2) == piece and self.__board.get_coords(r + 3, c - 3) == piece:

                    ok = 1
                    self.__board.set_coords(r + 4, c - 4, p2)
        return ok
    def get_coords(self, x, y):
        """
        function that passes the element on the board[x][y]
        :param x: row
        :param y: column
        :return: the coordinates
        """
        return self.__board.get_coords(x, y)
    def set_coords(self, x, y, new):
        """
        function that changes the coordinates
        :param x: row
        :param y: column
        :param new: the new element
        :return: -
        """
        self.__board.set_coords(x, y, new)

