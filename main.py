import random as rand
import os

width = int(input("Enter width of game here."))
height = int(input("Enter height of game here."))
total_squares = width * height
mines = int(input("Enter number of mines here."))
squares = []


def mine_available(squares, mines):
    pdm = 0
    for row in squares:
        for square in row:
            if square.is_mine:
                pdm += 1
    if pdm < int(mines):
        return True
    return False


class Square:
    creation_x = 0
    creation_y = 1

    mine_creation_list = []
    created_mines = 0
    while created_mines < mines:
        test_tuplet = (rand.randint(1, width), rand.randint(1, height))
        if test_tuplet not in mine_creation_list:
            mine_creation_list.append(test_tuplet)
            created_mines += 1

    def __init__(self,
                 dug=False,
                 is_mine=False,
                 flagged=False,
                 x=int,
                 y=int,
                 number=int):
        Square.creation_x += 1
        if Square.creation_x > width:
            Square.creation_y += 1
            Square.creation_x = 1
        self.x = Square.creation_x
        self.y = Square.creation_y

        self.is_mine = is_mine
        self.dug = dug
        self.flagged = flagged
        self.number = number

for i in range(int(height)):
    row = []
    for j in range(int(width)):
        row.append(Square())
    squares.append(row)


def print_space(text):
    print(text, end=" ")


def print_board():
    print_space("\u2a09")
    for i in range(1, width + 1):
        print_space(i)
    print()
    for i in range(height):
        print_space(i + 1)
        for j in range(width):
            if squares[i][j].dug:
                print_space(squares[i][j].number)
            elif squares[i][j].flagged:
                print_space("\u2690")
            else:
                print_space("\u25a1")
        print()


starter_square_x = int(
    input("Choose a starter square's x coordinate here.")) - 1
starter_square_y = int(
    input("Choose a starter square's y coordinate here.")) - 1
squares[starter_square_y][starter_square_x].dug = True
revealed_squares_percentage = 0
if starter_square_x == (0 or width - 1) and starter_square_y == (0 or
                                                                 height - 1):
    revealed_squares_percentage = 28
elif starter_square_x == (0 or width - 1) or starter_square_y == (0 or
                                                                  height - 1):
    revealed_squares_percentage = 34
elif starter_square_x != (0 or width - 1) and starter_square_y != (0 or
                                                                   height - 1):
    revealed_squares_percentage = 42
revealed_squares_int = int(revealed_squares_percentage / 100 * total_squares)

number_of_mines_percentage = 20

os.system("clear")


def game():
    running = True
    while running:
        print_board()
        action = input(
            "Enter action here. Either type \"d\" to dig, \"f\" to flag, or \"q\" to quit."
        )
        if action == "d":
            x = int(input("Enter x coordinate here.")) - 1
            y = int(input("Enter y coordinate here.")) - 1
            if squares[y][x].is_mine:
                print("BOOM!")
                running = False
            elif squares[y][x].flagged:
                print("There is a flag on this square.")
            else:
                squares[y][x].dug = True
                if squares[y][x].number == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= y + i < height and 0 <= x + j < width:
                                if squares[y + i][x + j].is_mine:
                                    squares[y + i][x + j].number += 1
            os.system("clear")
            print("Choose a square to dig.")
            x = int(input("Enter x coordinate here.")) - 1
            y = int(input("Enter y coordinate here.")) - 1
            if squares[y][x].is_mine:
                print("BOOM!")
                running = False
            elif squares[y][x].flagged:
                squares[y][x].flagged = False
                print("The flag on this square has been removed.")
            else:
                squares[y][x].dug = True
                if squares[y][x].number == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= y + i < height and 0 <= x + j < width:
                                if squares[y + i][x + j].is_mine:
                                    squares[y + i][x + j].number += 1
            os.system("clear")
        elif action == "f":
            print("Choose a square to flag.")
            x = int(input("Enter x coordinate here.")) - 1
            y = int(input("Enter y coordinate here.")) - 1
            if squares[y][x].flagged:
                print("Already flagged.")
            else:
                squares[y][x].flagged = True
            os.system("clear")
        elif action == "q":
            running = False
        else:
            os.system("clear")
        stw = 0
        for row in squares:
            for square in row:
                if not square.is_mine and square.dug:
                    stw += 1
        if stw == total_squares - mines:
            print("You win!")
            running = False


game()