from random import randint, seed
import time
start_time = time.time()

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


seed(41)

n = 100000
T = [randint(-1000, 1000) for i in range(n)]
# T = [6, 1, 4, 5, 2]

# print("przed sortowaniem: T =", T)
T = quicksort(T, 0, n)
# print("po sortowaniu    : T =", T)

# for i in range(len(T) - 1):
#     if T[i] > T[i + 1]:
#         print("Błąd sortowania!")
#         exit()

# print("OK")
print("--- %s seconds ---" % (time.time() - start_time))