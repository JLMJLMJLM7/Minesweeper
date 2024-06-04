import random
import os

def create_board(width, height, mines):
    board = [['*' for _ in range(width)] for _ in range(height)]

    mine_count = 0
    while mine_count < mines:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if board[y][x] != 'M':
            board[y][x] = 'M'
            mine_count += 1

    return board

def reveal_chunk(board, x, y, width, height, start):
    if x < 0 or x >= width or y < 0 or y >= height or board[y][x]!= '*':
        return

    if start and board[y][x] == 'M':
        board = create_board(width, height, mines)
    elif board[y][x] == 'M':
        print("You lose!")
        exit()

    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = x + i, y + j
            if 0 <= nx < width and 0 <= ny < height and board[ny][nx] == 'M':
                count += 1

    board[y][x] = str(count) if count > 0 else ''

    if count == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                reveal_chunk(board, nx, ny, width, height)
    elif count > 0:
        board[y][x] = str(count)

def print_board(board):
    print("    ", end="")
    for i in range(len(board[0])):
        print(f"{i+1:2}", end="  ")
    print()
    print("   +-" + "-" * (len(board[0]) * 4 - 1) + "-+")
    for i, row in enumerate(board):
        print(f" {i+1:2}|", end="")
        for cell in row:
            print(f" {cell}", end="  ")
        print(" |")
    print("   +-"+"-" * (len(board[0]) * 4 - 1) + "-+")

def main():
    while True:
        width = int(input("Enter the width of the board: "))
        if width <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        elif width > 100:
            print("Invalid input. Please enter an integer less than 100.")
            continue
        height = int(input("Enter the height of the board: "))
        if height <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        elif height > 100:
            print("Invalid input. Please enter an integer less than 100.")
            continue
        mines = int(input("Enter the number of mines: "))
        if mines <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        elif mines > width * height:
            print("Invalid input. Please enter an integer less than or equal to the number of cells on the board.")
            continue
        board = create_board(width, height, mines)
        print_board(board)
        break

    while True:
            try:
                x = int(input("Enter the x coordinate of the starting cell: ")) - 1
                y = int(input("Enter the y coordinate of the starting cell: ")) - 1
                reveal_chunk(x, y, width, height, height, True)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    while True:
        board = create_board(width, height, mines)
    
        os.system("clear")
        print_board(board)   

        while True:
            x = int(input("Enter the x coordinate of the next cell you want to dig: ")) - 1
            if x < 0 or x >= width:
                print("Invalid input. Please enter a valid integer.")
                continue
            y = int(input("Enter the y coordinate of the next cell you want to dig: ")) - 1
            if y < 0 or y >= height:
                print("Invalid input. Please enter a valid integer.")
                continue
            board = reveal_chunk(board, x, y, width, height, False)
            print_board(board)

if __name__ == '__main__':
    main()