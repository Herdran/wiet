"""Zadanie 19. Zadanie jak powyżej. Funkcja sprawdzająca czy król
może dostać się z pola w,k do któregokolwiek z narożników."""

from random import randint
from time import time

start_time = time()


def cw_19(x, y):
    vectors_list = [[(1, 1), (1, 0), (0, 1), (7, 7)], [(1, -1), (1, 0), (0, -1), (7, 0)],
               [(-1, 1), (-1, 0), (0, 1), (0, 7)], [(-1, -1), (-1, 0), (0, -1), (0, 0)]]

    def checking_numbers(number_1, number_2):
        n1 = number_1 % 10
        while number_2 > 9:
            number_2 //= 10
        n2 = number_2
        if n1 < n2:
            return True
        return False

    def if_move_possible(x, y, vector):
        if not (vector[0] == 0 <= x) or (vector[0] == 7 > x):
            return False
        if not (vector[1] == 0 <= y) or (y < vector[1] == 7 > y):
            return False
        print("nani")
        return True

    def func(x, y, vectors):
        if x + y != vectors[3][0] + vectors[3][1]:
            for i in range(3):
                if if_move_possible(x, y, vectors[3]) and checking_numbers(arr[x][y], arr[x + vectors[i][0]][y + vectors[i][1]]):
                    func(x + vectors[i][0], y + vectors[i][1], vectors)
                # if x < vectors[3][0] and y < vectors[3][1] and checking_numbers(arr[x][y], arr[x + 1][y + 1]):
                #     func(x + 1, y + 1, vectors)
                # if x < vectors[3][0] and checking_numbers(arr[x][y], arr[x + 1][y]):
                #     func(x + 1, y, vectors)
                # if y < vectors[3][1] and checking_numbers(arr[x][y], arr[x][y + 1]):
                #     func(x, y + 1, vectors)
        else:
            print("Moszna")
            print(time() - start_time)
            exit(0)

    for _ in vectors_list:
        func(x, y, _)

    return False


# arr = [[randint(10, 12) for _ in range(8)] for _ in range(8)]
arr = [[0, 9, 2, 3, 4, 5, 6, 8],
       [9, 9, 3, 4, 5, 6, 7, 81],
       [1, 2, 3, 4, 5, 6, 7, 2],
       [1, 2, 3, 4, 5, 6, 7, 3],
       [1, 2, 3, 4, 5, 6, 7, 4],
       [1, 2, 3, 4, 5, 6, 7, 5],
       [9, 9, 3, 4, 5, 6, 9, 9],
       [1, 9, 3, 4, 5, 6, 9, 7]]

# for _ in arr:
#     print(_)
print(cw_19(4, 5))
