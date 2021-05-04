import numpy as np

# board is a 9x9 numpy array
# pos (0,0) is top left of the board and pos (9,9) is bottom right
board = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]])


def controller():
    print('Solutions:\n')
    solver()


def solver():
    # solver
    # find board positions that contain '0'
    for y in range(0, 9):
        for x in range(0, 9):
            if board[y, x] == 0:
                # begin checking possible numbers
                for num in range(1, 10):
                    if can_place(y, x, num):
                        board[y, x] = num  # if num can be placed, place it
                        solver()           # then recursively call solver to continue solving
                        board[y, x] = 0    # if no more possible choices, then place '0' and backtrack
                return                     # return to last call if no empty space
    print(board)                           # print board, then continue finding solutions


# board consists of a 9x9 numpy array, this function checks to see if
# a specified number, called 'num', can be placed in the (y,x) position
# of the board
def can_place(y, x, num):
    # check the rows and cols for num with respect to the x and y coords
    for i in range(0, 9):
        if board[y, i] == num:  # check horizontal axis
            return False
    for i in range(0, 9):
        if board[i, x] == num:  # check vertical axis
            return False

    # take 3x3 local grid and check if num can be placed
    x_sub = (x // 3) * 3  # floor division finds either 0,1,2. then multiply by factor of 3
    y_sub = (y // 3) * 3  # floor division finds either 0,1,2. then multiply by factor of 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y_sub + i, x_sub + j] == num:  # if num lies on any square in the local grid, return false
                return False
    return True


if __name__ == '__main__':
    controller()
