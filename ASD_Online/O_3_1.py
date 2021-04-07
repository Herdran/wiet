from random import randint, seed
import time



def wird_radix_sort(T):
    n = len(T)

    A = [0]*n
    B = [0]*n

    for i in range(n):
        A[T[i] % n] += 1
    for i in range(1, n):
        A[i] += A[i-1]
    for i in range(n-1, -1, -1):
        A[T[i] % n] -= 1
        B[A[T[i] % n]] = T[i]

    A = [0]*n
    result = [0]*n

    for i in range(n):
        A[B[i] // n] += 1
    for i in range(1, n):
        A[i] += A[i-1]
    for i in range(n-1, -1, -1):
        A[B[i] // n] -= 1
        result[A[B[i] // n]] = B[i]


    for i in range(n):
        T[i] = result[i]



seed(42)

n = 1000000
T = [randint(0, n*n-1) for i in range(n)]
# print(T)
start_time = time.time()
wird_radix_sort(T)
# print(T)
print("--- %s seconds ---" % (time.time() - start_time))