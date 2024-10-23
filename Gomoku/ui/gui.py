import math

import pygame, sys

from src.service.service import Gameservice

class UI:
    @staticmethod
    def menu():
        print("Welcome to Gomoku game!")
        print("Don't forget that always black starts first!")
        print("You can place a stone only on the board choosing a row and a column!\n")
        print("Press 1 to play with a friend:")
        print("Press 2 to play with the computer:")
    def __init__(self, r, c):
        self.__board = Gameservice(r, c)
        self.column = c
        self.row = r
        self.squaresize = 70
        self.radius = int(self.squaresize / 2 - 5)
        self.width = (self.column) * self.squaresize
        self.height = (self.row) * self.squaresize
        self.screen = pygame.display.set_mode((self.width, self.height))
    def draw_board(self, col, row):
        BLUE = (6, 22, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        for c in range(1,col):
            for r in range(1,row):
                pygame.draw.rect(self.screen, BLUE, (c * self.squaresize, r * self.squaresize, self.squaresize, self.squaresize))
                pygame.draw.circle(self.screen, BLACK, (int(c * self.squaresize + self.squaresize / 2), int(r * self.squaresize + self.squaresize / 2)), self.radius)

        for c in range(1, col):
            for r in range(1, row):
                if self.__board.get_coords(r, c) == 1:
                    pygame.draw.circle(self.screen, YELLOW, (int(c * self.squaresize + self.squaresize / 2), int(r * self.squaresize + self.squaresize / 2)), self.radius)
                elif self.__board.get_coords(r, c) == 2:
                    pygame.draw.circle(self.screen, RED, (int(c * self.squaresize + self.squaresize / 2), int(r * self.squaresize + self.squaresize / 2)),self.radius)
        pygame.display.update()
    def create(self, column, row):
        pygame.init()
        self.draw_board(column, row)
        pygame.display.update()
        pygame.display.set_caption("Gomoku")
    def start(self, rows, cols):
        self.menu()
        option = str(input("->"))
        if option == "1":
            name1 = str(input("Player 1 enter your name:\n"))
            name2 = str(input("Player 2 enter your name:\n"))
            print("Start Game!\n")
            self.create(cols, rows)
            turn = 0
            game_over = False
            while not game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if turn == 0:
                            font = pygame.font.SysFont("monospace", 70)
                            RED = (255, 0, 0)
                            YELLOW = (255, 255, 0)
                            self.create(cols, rows)
                            self.__board.pass_board()
                            posx = event.pos[0]
                            posy = event.pos[1]
                            row = int(math.floor(posy / self.squaresize))
                            column = int(math.floor(posx / self.squaresize))
                            try:
                                self.__board.add_stone(row, column, 1)
                            except Exception as ex:
                                print(ex)
                            ok = self.__board.check_win(rows, cols, 1)
                            if ok == 1:
                                label = font.render(name1 + ", you won!", 1, YELLOW)
                                label2 = font.render("Congratulation!  ", True, YELLOW)
                                label2 = pygame.transform.rotate(label2, 90)
                                self.screen.blit(label, (100, 3))
                                self.screen.blit(label2, (5, 3))
                                print("Congratulation!"+ name1 +" you won!")
                                game_over = True
                                print(self.__board.pass_board())
                                self.draw_board(cols, rows)

                        else:
                            self.create(cols, rows)
                            font = pygame.font.SysFont("monospace", 70)
                            RED = (255, 0, 0)
                            YELLOW = (255, 255, 0)
                            posx = event.pos[0]
                            posy = event.pos[1]
                            row = int(math.floor(posy/self.squaresize))
                            column = int(math.floor(posx / self.squaresize))
                            try:
                                self.__board.add_stone(row, column, 2)
                            except ValueError as ve:
                                print(ve)
                            ok = self.__board.check_win(rows, cols, 2)
                            if ok == 1:
                                label = font.render(name2 + ", you won!", 1, RED)
                                label2 = font.render("Congratulation!  ", True, RED)
                                label2 = pygame.transform.rotate(label2, 90)
                                self.screen.blit(label, (100, 3))
                                self.screen.blit(label2, (5, 3))
                                print("Congratulation!" + name2 + "You won!")
                                game_over = True
                                print(self.__board.pass_board())
                                self.draw_board(cols, rows)
                        print(self.__board.pass_board())
                        self.draw_board(cols, rows)
                        turn += 1
                        turn = turn % 2
                        if game_over:
                            pygame.time.wait(5000)
        elif option == "2":
            name = str(input("Player 1 enter your name:"))
            print("Start Game!\n")
            game_over = False
            self.create(cols, rows)
            while not game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        font = pygame.font.SysFont("monospace", 70)
                        RED = (255, 0, 0)
                        YELLOW = (255, 255, 0)
                        self.create(cols, rows)
                        print(self.__board.pass_board())
                        posx = event.pos[0]
                        posy = event.pos[1]
                        row = int(math.floor((posy / self.squaresize)))
                        column = int(math.floor((posx / self.squaresize)))
                        try:
                            self.__board.add_stone(row, column, 1)
                        except Exception as ex:
                            print(ex)
                        ok = self.__board.check_win(rows, cols, 1)
                        if ok == 1:
                            label = font.render(name + ", you won!", 1, YELLOW)
                            label2 = font.render("Congratulation!  ", True, YELLOW)
                            label2 = pygame.transform.rotate(label2, 90)
                            self.screen.blit(label, (100, 3))
                            self.screen.blit(label2, (5, 3))
                            print("Congratulation!" + name + " you won!")
                            game_over = True
                            print(self.__board.pass_board())
                            self.draw_board(cols, rows)
                        self.__board.add_stone_ai(rows, cols, 1, 2)
                        ok = self.__board.check_win(rows, cols, 2)
                        if ok == 1:
                            label = font.render("You lost!", 1, RED)
                            self.screen.blit(label, (100, 3))
                            print("You lost!The ai won!")
                            game_over = True
                            print(self.__board.pass_board())
                            self.draw_board(cols, rows)
                        self.draw_board(cols, rows)
                        if game_over:
                            pygame.time.wait(5000)

        else:
            print("Invalid command! Try again!")




