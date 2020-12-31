table = [[8, 1, 0, 0, 3, 0, 0, 2, 7],
         [0, 6, 2, 0, 5, 0, 0, 9, 0],
         [0, 7, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 6, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 2, 0, 0, 0, 4],
         [0, 0, 8, 0, 0, 5, 0, 7, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 0],
         [0, 2, 0, 0, 1, 0, 7, 5, 0],
         [3, 8, 0, 0, 7, 0, 0, 4, 2]]


# find 0
# check if number is ok
# print table
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_zero(bo, x, y):
    if bo[x][y] == 0:
        return True
    else:
        return False


def possible(bo, x, y, n):
    for i in range(0, 9):
        if bo[i][y] == n:
            return False

    for j in range(0, 9):
        if bo[x][j] == n:
            return False

    x0 = (x // 3) + 3
    y0 = (y // 3) + 3
    for i in range(x0):
        for j in range(y0):
            if bo[i][j] == n:
                return False

    return True


def solve():
    for i in range(0, 9):
        for j in range(0, 9):
            if find_zero(table, i, j):
                for n in range(1, 9):
                    if possible(table, i, j, n):
                        table[i][j] = n
                        solve()


solve()
print_board(table)
