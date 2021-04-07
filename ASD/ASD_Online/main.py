from random import randint, seed
import time
start_time = time.time()

def quicksort(A, first_i, last_i):
    same = 0
    backspace = 0
    if first_i < last_i-1:
        pivot = A[last_i-1]
        empty = first_i
        for i in range(first_i, last_i - 1):
            if A[i] == pivot:
                same += 1
                backspace += 1
                print(A[i], A[last_i-1-backspace], i)
                A[i], A[last_i-1-backspace] = A[last_i-1-backspace], A[i]
            if A[i] < pivot:
                if empty != i:
                    A[empty], A[i] = A[i], A[empty]
                empty += 1
        print(A, "aaaa", empty)
        for i in range(same+1):
            A[empty+i], A[last_i-1-i] = A[last_i-1-i], A[empty+i]
        print(A)
        A = quicksort(A, first_i, empty-same)
        A = quicksort(A, empty + 1, last_i)
        return A
    else:
        return A


# seed(40)

n = 5
T = [randint(0, 3) for i in range(n)]
T = [0, 1, 2, 0, 2]

print("przed sortowaniem: T =", T)
T = quicksort(T, 0, n)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")
print("--- %s seconds ---" % (time.time() - start_time))