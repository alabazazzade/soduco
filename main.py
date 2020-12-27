# table = [[0, 7, 0, 0, 5, 0, 0, 6, 0],
#          [4, 0, 0, 9, 0, 3, 0, 0, 1],
#          [0, 0, 8, 0, 0, 0, 3, 0, 2],
#          [0, 5, 0, 0, 0, 0, 0, 4, 0],
#          [1, 0, 0, 0, 0, 0, 0, 0, 9],
#          [0, 2, 0, 0, 0, 0, 0, 1, 0],
#          [0, 0, 4, 0, 0, 0, 7, 0, 0],
#          [9, 0, 0, 1, 0, 7, 0, 0, 6],
#          [0, 8, 0, 0, 3, 0, 0, 5, 0]]
#
#
# def hor_col_line(sudo):
#     for i in range(len(sudo)):
#         if i % 3 == 0 and i != 0:
#             print('-----------------------------')
#         for j in range(len(sudo[0])):
#             if j % 3 == 0 and j != 0:
#                 print('|', end='')
#             if j == 8:
#                 print(sudo[i][j])
#             else:
#                 print(f'{sudo[i][j]} '+' ', end='')
#
#
# def Find_empty(sudo):
#     for i in range(len(sudo)):
#         for j in range(len(sudo[0])):
#             if sudo[i][j] == 0:
#                 return i, j
#     return None
#
#
# def check_valid(sudo, num, pos):
#     # check row
#
#     for item in range(len(sudo[0])):
#         if item == num and pos[1] != num:
#             return False
#
#     # check col
#     for item in range(len(sudo)):
#         if item == num and pos[0] != num:
#             return False
#
#     # check boxes
#     row = pos[1] // 3
#     col = pos[0] // 3
#     for item in range(3*row, 3 * row + 3):
#         for itt in range(3*col, 3 * col + 3):
#             if itt == num and (item, itt) != pos:
#                 return False
#
#     return True
#
#
# def solve(sudo):
#     find = Find_empty(table)
#     if not find:
#         return True
#     else:
#         (i, j) = Find_empty(table)
#
#     for num in range(1, 10):
#         if check_valid(table, num, (i, j)):
#             sudo[i][j] = num
#             if solve(sudo):
#                 return True
#             sudo[i][j] = 0
#     return False
#
#
# hor_col_line(table)
# print('========================')
# solve(table)
# hor_col_line(table)
table = [[0, 7, 0, 0, 5, 0, 0, 6, 0],
         [4, 0, 0, 9, 0, 3, 0, 0, 1],
         [0, 0, 8, 0, 0, 0, 3, 0, 2],
         [0, 5, 0, 0, 0, 0, 0, 4, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 9],
         [0, 2, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 4, 0, 0, 0, 7, 0, 0],
         [9, 0, 0, 1, 0, 7, 0, 0, 6],
         [0, 8, 0, 0, 3, 0, 0, 5, 0]]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


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


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None



print_board(table)
solve(table)
print_board(table)
