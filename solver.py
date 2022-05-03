"""Sudoku solver"""
"""Michael Zhou"""


board = [
    [4,0,0,0,0,0,0,0,2],
    [1,6,2,7,0,4,5,9,8],
    [0,0,8,0,1,9,7,6,0],
    [2,5,0,0,0,7,6,0,0],
    [0,0,7,3,0,0,9,1,0],
    [9,1,0,5,0,0,4,2,0],
    [0,0,5,0,0,0,0,0,0],
    [7,0,6,0,5,1,0,0,0],
    [8,9,0,0,0,3,2,0,6]
]


def solve(bor):
    find = findEmpty(bor)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bor, i, (row, col)):
            bor[row][col] = i

            if solve(bor):
                return True

            bor[row][col] = 0

    return False


def valid(bor, num, pos):

    for i in range(len(bor[0])):
        if bor[pos[0]][i] == num and pos[1] != i:
            return False


    for i in range(len(bor)):
        if bor[i][pos[1]] == num and pos[0] != i:
            return False


    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bor[i][j] == num and (i,j) != pos:
                return False

    return True


def printBoard(bor):
    for i in range(len(bor)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bor[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bor[i][j])
            else:
                print(str(bor[i][j]) + " ", end="")


def findEmpty(bor):
    for i in range(len(bor)):
        for j in range(len(bor[0])):
            if bor[i][j] == 0:
                return (i, j)

    return None

printBoard(board)
solve(board)
print("___________________")
printBoard(board)
