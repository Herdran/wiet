"""Zadanie 20. Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do
któregokolwiek z narożników"""

from random import randint
from time import time


T = [[randint(0, 10) for _ in range(8)] for _ in range(8)]

vectors = [[(1, 1), (1, 0), (0, 1)],
           [(1, -1), (1, 0), (0, -1)],
           [(-1, 1), (-1, 0), (0, 1)],
           [(-1, -1), (-1, 0), (0, -1)]]


def get_first_digit(n):
    while n > 9:
        n //= 10
    return n


def is_possible(T, row, col, last_number):
    if row > 7 or col > 7 or row < 0 or col < 0:
        return False

    if last_number % 10 > get_first_digit(T[row][col]):
        return False
    return True


def kingu(row, col, corner, path, flag=True):

    if row == col == 7 or row == col == 0 or (row == 7 and col == 0) or (row == 0 and col == 7):
        print("Yaaaaaas")
        print(path + " FINISH")
        print(time() - start_time)
        exit(0)

    for v in vectors[corner]:
        row_ = row + v[0]
        col_ = col + v[1]
        if is_possible(T, row_, col_, T[row][col]):
            kingu(row_, col_, corner, f'{path} [{row_}][{col_}] -->', False)

    if flag:
        # print(time() - start_time)
        print("Nieee")



# gg = [[0, 1, 2, 3, 4, 5, 6, 7],
#        [1, 2, 3, 4, 5, 6, 7, 81],
#        [1, 2, 3, 4, 5, 6, 7, 2],
#        [1, 2, 3, 4, 5, 6, 7, 3],
#        [1, 2, 3, 4, 5, 6, 7, 4],
#        [1, 2, 3, 4, 5, 6, 7, 5],
#        [1, 2, 3, 4, 5, 6, 7, 6],
#        [1, 2, 3, 4, 5, 6, 7, 7]]

T = [[0, 9, 2, 3, 4, 5, 6, 8],
       [9, 9, 3, 4, 5, 6, 7, 81],
       [1, 2, 3, 4, 5, 6, 7, 2],
       [1, 2, 3, 4, 1, 6, 7, 3],
       [1, 2, 3, 4, 5, 6, 7, 4],
       [1, 2, 3, 4, 5, 6, 7, 5],
       [9, 9, 3, 4, 5, 6, 9, 9],
       [1, 9, 3, 4, 5, 6, 9, 7]]


start_time = time()
for corner in range(4):
    kingu(3, 3, corner, "[3][3] -->")