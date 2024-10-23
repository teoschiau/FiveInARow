from src.service.service import Gameservice


class UI:
    @staticmethod
    def menu():
        print("Welcome to Gomoku game!")
        print("Don't forget that always black starts first!")
        print("You can place a stone only on the board choosing a row and a column!")
        print("First player plays with one and the second one with 2!")
        print("Press 1 to play with a friend:")
        print("Press 2 to play with the computer:\n")

    def __init__(self, r, c):
        self.__board = Gameservice(r, c)

    def start(self, rows, cols):
        self.menu()
        option = str(input("->"))
        if option == "1":
            name1 = str(input("Player 1 enter your name:"))
            name2 = str(input("Player 2 enter your name:"))
            print("Start Game!\n")
            turn = 0
            game_over = False
            while not game_over:
                if turn == 0:
                    print(self.__board.pass_board())
                    print(name1 +" where would you like to put your stone?")
                    row = int(input("Please select a row:(1-10)\n->"))
                    column = int(input("Please select a column:(1-10)\n->"))
                    try:
                        self.__board.add_stone(row, column, 1)
                    except Exception as ex:
                        print(ex)
                    ok = self.__board.check_6(rows, cols, 1)
                    if ok == 1:
                        print("Congratulation!" + name2 + " you won because of the outline!")
                        game_over = True
                        print(self.__board.pass_board())
                    ok = self.__board.check_win(rows, cols, 1)
                    if ok == 1:
                        print("Congratulation!"+ name1 +" you won!")
                        game_over = True
                        print(self.__board.pass_board())

                else:
                    print(self.__board.pass_board())
                    print(name2 + " where would you like to put your stone?")
                    row = int(input("Please select a row:(1-10)\n->"))
                    column = int(input("Please select a column:(1-10)\n->"))
                    try:
                        self.__board.add_stone(row, column, 2)
                    except ValueError as ve:
                        print(ve)
                    ok = self.__board.check_6(rows, cols, 2)
                    if ok == 1:
                        print("Congratulation!"+ name1 +" you won because of the outline!")
                        game_over = True
                        print(self.__board.pass_board())
                    ok = self.__board.check_win(rows, cols, 2)
                    if ok == 1:
                        print("Congratulation!" + name2 + "You won!")
                        game_over = True
                        print(self.__board.pass_board())
                turn += 1
                turn = turn % 2
        elif option == "2":
            name = str(input("Player 1 enter your name:"))
            print("Start Game!\n")
            game_over = False
            while not game_over:
                print(self.__board.pass_board())
                print(name + " where would you like to put your stone?")
                row = int(input("Please select a row:(1-10)\n->"))
                column = int(input("Please select a column:(1-10)\n->"))
                try:
                    self.__board.add_stone(row, column, 1)
                except Exception as ex:
                    print(ex)

                ok = self.__board.check_6(rows, cols, 1)
                if ok == 1:
                    print("You lost!The ai won because of the outline!")
                    game_over = True
                    print(self.__board.pass_board())
                ok = self.__board.check_win(rows, cols, 1)
                if ok == 1:
                    print("Congratulation!" + name + " you won!")
                    game_over = True
                    print(self.__board.pass_board())
                self.__board.add_stone_ai(rows, cols, 1, 2)
                ok = self.__board.check_6(rows, cols, 2)
                if ok == 1:
                    print("Congratulation!" + name + " you won because of the outline!")
                    game_over = True
                    print(self.__board.pass_board())
                ok = self.__board.check_win(rows, cols, 2)
                if ok == 1:
                    print("You lost!The ai won!")
                    game_over = True
                    print(self.__board.pass_board())

        else:
            print("Invalid command! Try again!")
