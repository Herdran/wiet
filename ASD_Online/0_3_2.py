from random import randint, seed
from math import log10
import time


def quicksort(A, first_i, last_i):
    if first_i < last_i-1:
        pivot = A[last_i-1]
        empty = first_i
        for i in range(first_i, last_i - 1):
            if A[i] < pivot:
                A[empty], A[i] = A[i], A[empty]
                empty += 1
        A[empty], A[last_i-1] = A[last_i-1], A[empty]
        A = quicksort(A, first_i, empty)
        A = quicksort(A, empty + 1, last_i)
        return A
    else:
        return A


def binary_search(T, el, a, b):
    if a > b:
        return None
    c = (a + b) // 2
    if T[c][0] == el:
        key = binary_search(T, el, a, c - 1)
        if key == None:
            return c
    elif T[c][0] > el:
        return binary_search(T, el, a, c - 1)
    else:
        return binary_search(T, el, c + 1, b)


def radigz(T):
    length = len(T)
    x = log10(n)
    if x % 1 != 0:
        x = int(x // 1 + 1)
    else:
        x = int(x)

    A = []
    for i in range(length):
        if not (T[i], 0) in A:
            A.append((T[i], 0))
    # for i in range(length):
    #     if not binary_search(A, T[i], 0, len(A) - 1):
    #         A.append((T[i], 0))
    #     else:


    A = quicksort(A, 0, x)

    for i in range(length):
        left = 0
        right = len(A) - 1
        while left != right:
            tmp = (left + right) // 2
            if A[tmp][0] < T[i]:
                left = tmp + 1
            elif A[tmp][0] > T[i]:
                right = tmp - 1
            else:
                left = tmp
                right = left
        A[left] = (A[left][0], A[left][1] + 1)
    index = 0
    for i in range(x):
        for j in range(A[i][1]):
            T[index] = A[i][0]
            index += 1


seed(42)

n = 1000
x = log10(n)
# print(x)
if x % 1 != 0:
    x = int(x // 1 + 1)
else:
    x = int(x)
# print(x)
T = [randint(0, x-1) for i in range(n)]
# print(T)
start_time = time.time()
radigz(T)
print("--- %s seconds ---" % (time.time() - start_time))
# print(T)

x = T[0]
for i in range(len(T)):
    if T[i] > x:
        x = T[i]
    elif T[i] < x:
        print("łijułiju")
        break