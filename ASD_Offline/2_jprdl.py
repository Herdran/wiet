from random import randint, seed
import time
start_time = time.time()

class Node:
    def __init__(self):
        self.next = None
        self.value = None


def quicksort(L, start, length):
    if length > 0:
        # printlist(L)
        curr = L
        pivot = curr
        curr = curr.next

        right_len = 0
        left_len = 0
        tmp = pivot
        pivot.next = None
        fajnal = 0
        same_numbers = False
        counter = 0
        # print("aaaaaaaaaa")
        # printlist(curr)
        # printlist(pivot)
        # print(length)
        for i in range(length - start):
            if curr.value > pivot.value:
                tmp.next = curr
                tmp = tmp.next
                curr = curr.next
                tmp.next = None
                right_len += 1
            elif curr.value < pivot.value:
                if not fajnal:
                    fajnal = curr
                    tmp_2 = curr
                else:
                    tmp_2.next = curr
                    tmp_2 = tmp_2.next
                curr = curr.next
                left_len += 1
            else:
                if not same_numbers:
                    same_numbers = curr
                    same_numbers_end = curr
                else:
                    same_numbers_end.next = curr
                    same_numbers_end = same_numbers_end.next
                # same_numbers_end = None
                curr = curr.next
                counter += 1
                # if not same_numbers:
                #     tmp = curr
                #     same_numbers = True
                # # tmp_2 = curr.next
                # if right_len > 0:
                #     tmp_2 = pivot.next
                # pivot.next = curr
                # curr = curr.next
                # if right_len > 0:
                #     pivot.next.next = tmp_2
            # print("łałałałała")
            # if fajnal:
            #     printlist(fajnal)
            # else:
            #     printlist(L)
        if fajnal:
            L = fajnal
            tmp_2.next = pivot
        # print("======================")
        # printlist(L)
        # printlist(pivot)
        # if same_numbers:
        #     printlist(same_numbers)
        if same_numbers:
            pivot.next, same_numbers_end.next = same_numbers, pivot.next
        # print("======================")
        # printlist(L)
        # printlist(pivot)
        # if same_numbers:
        #     printlist(same_numbers)
        for i in range(counter):
            pivot = pivot.next
        # printlist(pivot)
        L = quicksort(L, 0, left_len - 1)
        # print("======================")
        # print("======================")
        pivot.next = quicksort(pivot.next, 0, right_len - 1)
        if left_len > 1:
            tmp = L
            while tmp.next:
                tmp = tmp.next
            tmp.next = pivot
        return L
    return L


def qsort(L):
    tmp = L
    counter = 0
    while tmp.next:
        counter += 1
        tmp = tmp.next
    return quicksort(L, 0, counter)


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
T = [randint(1, 10) for i in range(n)]
# T = [1, 1, 1, 5, 2]
L = tab2list(T)

# print("przed sortowaniem: L =", end=" ")
# printlist(L)
L = qsort(L)
# print("po sortowaniu    : L =", end=" ")
# printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
print("--- %s seconds ---" % (time.time() - start_time))