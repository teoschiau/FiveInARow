import unittest

from src.service.service import Gameservice


class MyTestCase(unittest.TestCase):
    def test_coordinates(self):
        self.__board = Gameservice(3, 3)
        self.__board.set_coords(1, 1, 7)
        self.assertEqual(self.__board.get_coords(1,1), 7)

    def test_adding(self):
        self.__board = Gameservice(3, 3)
        self.__board.add_stone(2, 1, 30)
        self.assertEqual(self.__board.get_coords(2, 1), 30)

    def test_check_win(self):
        self.__board = Gameservice(10, 10)
        self.__board.set_coords(1, 1, 7)
        self.__board.set_coords(2, 2, 7)
        self.__board.set_coords(3, 3, 7)
        self.__board.set_coords(4, 4, 7)
        self.__board.set_coords(5, 5, 7)
        self.assertEqual(self.__board.check_win(10, 10, 7), 1)

    def test_ai(self):
        self.__board = Gameservice(10,10)
        self.__board.set_coords(1, 1, 7)
        self.__board.set_coords(2, 2, 7)
        self.__board.set_coords(3, 3, 7)
        self.__board.set_coords(4, 4, 7)
        self.__board.add_stone_ai(10, 10, 7, 8)
        self.assertEqual(self.__board.get_coords(5, 5), 8)

        
if __name__ == '__main__':
    unittest.main()
