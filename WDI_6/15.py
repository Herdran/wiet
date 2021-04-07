"""Zadanie 15. Problem 8 Hetmanów (treść oczywista)"""
from time import time
start_time = time()
def func(col, row):
    if not queens_positions:
        queens_positions.append((col, row))
        return True
    else:
        for i in queens_positions:
            if i[1] == row:
                return False
            if i[0]+i[1] == col+row:
                return False
            if i[0]-i[1] == col-row:
                return False
        queens_positions.append((col, row))
        return True


def printing(t):
    for i in t:
        print(i[1]+1, end=" ")
    print()


def cw_15(i):
    if i == N:
        # print(queens_positions)
        printing(queens_positions)
        # tmp[0] += 1
        del queens_positions[-1]
    else:
        for j in range(N):
            if func(i, j):
                cw_15(i + 1)
        if queens_positions:
            del queens_positions[-1]


N = 8
arr = [[0 for _ in range(N)] for _ in range(N)]
queens_positions = []
# tmp = [0]
cw_15(0)
# print(tmp)
print(time() - start_time)
