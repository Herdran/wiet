from math import log2, ceil, log10
from random import randint, seed
import time

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


def partition(T, a, b):
    pivot = T[b][0]
    i = a - 1
    for j in range(a, b):
        if T[j][0] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[b] = T[b], T[i + 1]
    return i + 1


def quicksort(T, a, b):
    if a < b:
        c = partition(T, a, b)
        quicksort(T, a, c - 1)
        quicksort(T, c + 1, b)


def sort_logn_diff(T):
    n = len(T)
    different = [[float("inf"), 0] for _ in range(ceil(log2(n)) + 1)]

    ind = -1
    for i in range(n):
        key = binary_search(different, T[i], 0, len(different) - 1)
        if key == None:
            ind += 1
            different[ind][0] = T[i]
            different[ind][1] = 1
            quicksort(different, 0, ind)
        else:
            different[key][1] += 1

    ind = 0
    for i in range(len(different)):
        for _ in range(different[i][1]):
            T[ind] = different[i][0]
            ind += 1


# T = [6, 2, 3, 2, 6, 3, 3, 2]
seed(42)

n = 1000000
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
sort_logn_diff(T)
print("--- %s seconds ---" % (time.time() - start_time))
# print(T)
x = T[0]
for i in range(len(T)):
    if T[i] > x:
        x = T[i]
    elif T[i] < x:
        print("łijułiju")
        break