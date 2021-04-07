from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def quicksort(L, start, length):
    # printlist(L)
    if length - start > 0:
        curr = L
        for i in range(start):
            curr = curr.next
        pivot = curr
        prev = L
        curr = curr.next
        if start > 1:
            for i in range(start - 1):
                prev = prev.next

        right_len = 0
        left_len = 0
        tmp = pivot
        B = 0
        pivot.next = None
        fajnal = 0
        konjec = 0

        # print(curr.value, length, start, pivot.value, "dataaaaaaaaaa")


        for i in range(length - start):
            if curr.value > pivot.value:
                if not konjec:
                    konjec = curr
                tmp.next = curr
                tmp = tmp.next
                curr = curr.next
                tmp.next = None
                right_len += 1
            else:
                if not fajnal:
                    fajnal = curr
                    tmp_2 = curr
                else:
                    tmp_2.next = curr
                    tmp_2 = tmp_2.next
                curr = curr.next
                left_len += 1

        printlist(pivot)
        print("bambarabamboro")

        if fajnal:
            L = fajnal
            tmp_2.next = pivot

        L = quicksort(L, 0, left_len - 1)

        print("//////////////////////////")
        printlist(L)
        print("//////////////////////////")
        printlist(pivot)
        print(left_len, right_len)
        print("+++++++++++++")

        print("barararararar")
        printlist(pivot)
        printlist(L)
        # printlist(tmp)
        pivot.next = quicksort(pivot.next, 0, right_len - 1)
        # if tmp:
        if left_len > 1:
            tmp = L
            while tmp.next:
                tmp = tmp.next
            printlist(tmp)
            tmp.next = pivot
            printlist(tmp)
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        printlist(L)
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        # printlist(L)
        # print("----------------")
        printlist(pivot)
        print("=================")

        # if tmp_2:
        #     printlist(tmp_2)
        # if tmp:
        #     printlist(tmp)
        # if konjec:
        #     printlist(konjec)
        # print("--------", left_len, right_len)


        # L = quicksort(L, 0, left_len - 1)
        # if konjec:
        #     B = quicksort(konjec, 0, right_len - 1)
        # printlist(L)
        # print("fajnali")
        # if B:
        #     printlist(B)
        #     pivot.next = B
        # print("wadafak")
        # printlist(L)
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


seed(42)

n = 1000
T = [randint(1, 10) for i in range(n)]
# T = [8, 4, 1, 10, 9]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

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
