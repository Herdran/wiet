from random import randint, seed
from math import fabs
import time
start_time = time.time()


def get_median(A, first_i, last_i):
    j = 0
    if first_i - last_i < 2:
        return A[first_i], first_i
    while True:
        left = 0
        right = 0
        same = 1
        # print(first_i, last_i)
        pivot = A[first_i + j]
        for i in range(first_i, last_i):
            if i != first_i+j:
                if A[i] < pivot:
                    left += 1
                elif A[i] == pivot:
                    same += 1
                else:
                    right += 1
        if (left == right or same > fabs(left-right)):
            break
        j += 1
    return pivot, first_i+j




def quicksort(A, first_i, last_i):
    if first_i < last_i-1:
        pivot, pivot_id = get_median(A, first_i, last_i)
        empty = first_i
        for i in range(first_i, last_i):
            if i != pivot_id:
                if empty == pivot_id:
                    empty += 1
                if A[i] < pivot:
                    A[empty], A[i] = A[i], A[empty]
                    empty += 1
        # print(A)
        if empty > pivot_id:
            empty -= 1
        A[empty], A[pivot_id] = A[pivot_id], A[empty]
        # print(A)
        # print(first_i, last_i, empty)
        A = quicksort(A, first_i, empty)
        A = quicksort(A, empty + 1, last_i)
        return A
    else:
        return A


seed(40)

n = 1000000
T = [randint(-1000, 1000) for i in range(n)]
# T = [6, 4, 2, 5, 2, 9, 5, 10, 5]

# print("przed sortowaniem: T =", T)
T = quicksort(T, 0, n)
# print("po sortowaniu    : T =", T)
# for i in range(len(T) - 1):
#     if T[i] > T[i + 1]:
#         print("Błąd sortowania!")
#         exit()
#
# print("OK")
print("--- %s seconds ---" % (time.time() - start_time))

