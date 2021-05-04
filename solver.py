import numpy as np
import random as rn

# board is a 9x9 numpy array
# pos (0,0) is top left of the board and pos (9,9) is bottom right
# board = np.array([[0, 3, 0, 6, 0, 0, 0, 0, 1],
#                  [1, 0, 2, 0, 0, 7, 6, 0, 0],
#                  [9, 6, 4, 3, 2, 0, 7, 0, 8],
#                  [4, 0, 3, 0, 0, 0, 9, 0, 5],
#                  [0, 2, 6, 4, 0, 9, 0, 0, 7],
#                  [0, 1, 0, 7, 5, 3, 0, 6, 2],
#                  [2, 0, 1, 0, 3, 4, 5, 0, 0],
#                  [3, 5, 0, 0, 0, 0, 0, 2, 0],
#                  [6, 4, 8, 2, 7, 0, 1, 0, 0]])


def controller():
    print('\nGenerating new board...\n')
    board = generate_board()
    print(board)
    print('\nSolutions:\n')
    solver(board)
    print('\nDone\n')


# generate_board function creates a new and completely random sudoku board
# note that the board will not always be solvable, or may have many solutions
def generate_board():
    # create numpy array with shape of board and filled with zeros
    b = np.zeros((9, 9), dtype=int)
    counter = 0  # counter used to determine how many spots will be filled with numbers
    while counter != 25:
        y = rn.randint(0, 8)         # generate random y position
        x = rn.randint(0, 8)         # generate random x position
        num = rn.randint(1, 9)       # generate potential number to fill spot
        if can_place(y, x, num, b):  # if num can be placed on board according to sudoku rules
            b[y, x] = num            # then place it on board at x and y pos
            counter = counter + 1    # and increase counter
    return b


# solver function that solves puzzle recursively
def solver(b):
    # find board positions that contain '0'
    for y in range(0, 9):
        for x in range(0, 9):
            if b[y, x] == 0:
                # begin checking possible numbers
                for num in range(1, 10):
                    if can_place(y, x, num, b):
                        b[y, x] = num      # if num can be placed, place it
                        solver(b)          # then recursively call solver to continue solving
                        b[y, x] = 0        # if no more possible choices, then place '0' and backtrack
                return                     # return to last call if no empty space
    print(b)                               # print solved board
    input('\nContinue generating solutions?\n')


# board consists of a 9x9 numpy array, this function checks to see if
# a specified number, called 'num', can be placed in the (y,x) position
# of the board
def can_place(y, x, num, b):
    # check the rows and cols for num with respect to the x and y coords
    for i in range(0, 9):
        if b[y, i] == num:  # check horizontal axis
            return False
    for i in range(0, 9):
        if b[i, x] == num:  # check vertical axis
            return False

    # take 3x3 local grid and check if num can be placed
    x_sub = (x // 3) * 3  # floor division finds either 0,1,2. then multiply by factor of 3
    y_sub = (y // 3) * 3  # floor division finds either 0,1,2. then multiply by factor of 3
    for i in range(0, 3):
        for j in range(0, 3):
            if b[y_sub + i, x_sub + j] == num:  # if num lies on any square in the local grid, return false
                return False
    return True


if __name__ == '__main__':
    controller()
