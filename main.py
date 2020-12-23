table = [[0, 7, 0, 0, 5, 0, 0, 6, 0],
         [4, 0, 0, 9, 0, 3, 0, 0, 1],
         [0, 0, 8, 0, 0, 0, 3, 0, 0],
         [0, 5, 0, 0, 0, 0, 0, 4, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 9],
         [0, 2, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 4, 0, 0, 0, 7, 0, 0],
         [9, 0, 0, 1, 0, 7, 0, 0, 6],
         [0, 8, 0, 0, 3, 0, 0, 5, 0]]


def hor_col_line(sodu):
    i = 0
    for i in range(len(sodu)):
        if i % 3 == 0 and i != 0:
            print('-----------------------')
        for j in range(len(sodu[0])):
             if j % 3 == 0 and j != 0:
                print('|', end='')
             if j == 8:
                print(sodu[i][j])
             else:
                print(f'{sodu[i][j]} ',end = '')


def Find_zaro(sodu, cnt):
    for i in range(len(sodu)):
        for j in range(len(sodu[0])):
            if sodu[i][j] == 0 and cnt == 0:
                cnt = 1
                return i, j


def check_row(sodu,i , j):
    x=1
    for item in sodu:
        for m in range(len(sodu)):
            for n in range(len(sodu[0])):
               if sodu[m][n] == x:
                  x += 1
               else:
                  sodu[m][n] = x
                  break


def check_col(sodu,i , j):
    x=1
    for item in sodu:
        for m in range(len(sodu[0])):
            for n in range(len(sodu)):
               if sodu[m][n] == x:
                  x += 1
               else:
                  sodu[m][n] = x
                  break


cnt = 0
(j, i) = Find_zaro(table, cnt)
cnt = 0
(j, i) = Find_zaro(table, cnt)
check_row(table, i, j)
check_col(table, i, j)
hor_col_line(table)
