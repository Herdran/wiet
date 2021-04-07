from random import randint, seed
import time
start_time = time.time()

class Node:
    def __init__(self):
        self.next = None
        self.value = None


def quicksort(L, length):
    if length > 0:
        curr = L.next
        pivot = L
        pivot_end = pivot
        pivot.next = None
        right_len = 0
        left_len = 0
        left = 0
        same_numbers = False
        counter = 0
        for i in range(length):
            if curr.value > pivot.value:
                pivot_end.next = curr
                pivot_end = pivot_end.next
                curr = curr.next
                pivot_end.next = None
                right_len += 1
            elif curr.value < pivot.value:
                if not left:
                    left = curr
                    left_end = curr
                else:
                    left_end.next = curr
                    left_end = left_end.next
                curr = curr.next
                left_len += 1
            else:
                if not same_numbers:
                    same_numbers = curr
                    same_numbers_end = curr
                else:
                    same_numbers_end.next = curr
                    same_numbers_end = same_numbers_end.next
                curr = curr.next
                counter += 1

        if left:
            L = left
            left_end.next = pivot

        if same_numbers:
            pivot.next, same_numbers_end.next = same_numbers, pivot.next

        pivot_last = pivot
        for i in range(counter):
            pivot_last = pivot_last.next

        L = quicksort(L, left_len - 1)
        pivot_last.next = quicksort(pivot_last.next, right_len - 1)

        if left_len > 1:
            pivot_end = L
            while pivot_end.next:
                pivot_end = pivot_end.next
            pivot_end.next = pivot

        return L
    return L


def qsort(L):
    tmp = L
    counter = 0
    while tmp.next:
        counter += 1
        tmp = tmp.next
    return quicksort(L, counter)


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")



seed(45)

n = 1000000
T = [randint(-1000, 1000) for i in range(n)]
L = tab2list(T)

# print("przed sortowaniem: L =", end=" ")
# printlist(L)
L = qsort(L)
# print("po sortowaniu    : L =", end=" ")
# printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

# P = L
# while P.next != None:
#     if P.value > P.next.value:
#         print("Błąd sortowania")
#         exit(0)
#     P = P.next


print("OK")
print("--- %s seconds ---" % (time.time() - start_time))