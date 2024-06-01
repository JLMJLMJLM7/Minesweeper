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

    def __init__(self, dug=False, is_mine=bool, flagged=bool, x=int, y=int, number=int):
        creation_x += 1
        if creation_x > width:
            creation_y += 1
            creation_x = 1
        self.x = creation_x
        self.y = creation_y

        self.is_mine = is_mine
        self.dug = dug
        self.flagged = flagged
        self.number = number

for i in range(int(height)):
    row = []
    for j in range(int(width)):
        row.append(Square())
    squares.append(row)

def print_space(print):
    print(print, end=" ")

def print_board():
    print_space("\u2a09")
    for i in range(width + 1):
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



def game():
    while running:
        print_board()
        action = input("Enter action here. Either type \"d\" to dig, \"f\" to flag, or \"q\" to quit.")
        if action == "d":
            print("Choose a square to dig.")
            x = int(input("Enter x coordinate here.")) - 1
            y = int(input("Enter y coordinate here.")) - 1
            if squares[y][x].is_mine:
                print("BOOM!")
                running = False
            elif squares[y][x].flagged:
                print("There is a flag on this square.")
            else:
                squares[y][x].dug = True
                if squares[y][x].is_mine:
                    print("BOOM!")
                    running = False
                elif squares[y][x].number == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if squares[y+i][x+j].is_mine:
                                squares[y+i][x+j].number += 1
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
                if squares[y][x].is_mine:
                    print("BOOM!")
                    running = False
                elif squares[y][x].number == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if squares[y+i][x+j].is_mine:
                                squares[y+i][x+j].number += 1
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