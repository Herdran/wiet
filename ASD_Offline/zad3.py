from random import randint, shuffle, seed
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


def partition(T, a, b, index=-1):
    if index == -1:
        index = b
    pivot = T[index]
    i = a
    for j in range(a, b):
        if T[j] < pivot:
            T[i], T[j] = T[j], T[i]
            if i == index:
                index = j
            i += 1

    T[i], T[index] = T[index], T[i]
    return i


def select(A, p, r, k):
    if p == r:
        return A[p]

    q = partition(A, p, r)

    if q == k:
        return A[q]
    elif k < q:
        return select(A, p, q-1,k)
    else:
        return select(A, q+1, r, k)


def median_of_five(i, length, index):
    # wyznaczam left jako indeks pierwszego elementu z przedziału których będę szukać mediany i right jako indeks o jeden
    # większy niż indeks ostatniego elementu tego przedziału
    left = i * 5
    if (i + 1) * 5 > length - 1:
        right = length
    else:
        right = (i + 1) * 5

    bigger, smaller = 0, 0

    # sprawdzam czy długość sprawdzanego przedziału jest nieparzysta, jeśli jest to szukam mediany, jeśli nie to wartości
    # mniejszej z dwóch składowych mediany
    # funkcja bierze pierwszy element z przedziału i sprawdza ile jest mniejszych a ile większych od niej elementów w tym
    # przedziale, jeśli tyle samo to jest to mediana, jeśli nie to sprawdza kolejny
    if (right - left) % 2 != 0:
        median = left
        if right - left != 1:
            median -= 1
            while smaller == 0 or smaller != bigger:
                median += 1
                smaller = 0
                bigger = 0
                for i in range(left, right):
                    if i != median:
                        if A[i] > A[median]:
                            bigger += 1
                        else:
                            smaller += 1
        A[index], A[median] = A[median], A[index]
        index += 1
    else:
        median = left - 1
        while smaller == 0 or smaller != bigger:
            median += 1
            smaller = 1
            bigger = 0
            for i in range(left, right):
                if i != median:
                    if A[i] > A[median]:
                        bigger += 1
                    else:
                        smaller += 1
        A[index], A[median] = A[median], A[index]
        index += 1


def linearselect(A, k):
    length = len(A)
    # wyznaczam ilość przedziałów i zapisuję do zmiennej x
    x = length / 5
    if x % 1 != 0:
        x = int(x // 1 + 1)
    else:
        x = int(x)
    index = 0

    # wyznaczam medianę dla każdego z przedziałów, ustawiając ją na kolejne miejsca w tablicy, zaczynając od zerowego
    for i in range(x):
        median_of_five(i, length, index)
        index += 1

    # wyznaczam medianę median, czyli medianę elementów od 0 do x
    median_of_five(0, x, 0)

    # mediana median jest teraz na zerowym miejscu w tablicy, wykonuję funkcję partition dla jej wartości
    q = partition(A, 0, length, 0)

    # sprawdzam czy indeks uzyskany z funkcji partition jest szukanym, jeśli nie to wywołuję rekurencyjnie funkcję select
    # dla lewego lub prawego przedziału, w zależności od szukanego indeksu
    if q == k:
        return A[q]
    elif k < q:
        return select(A, 0, q-1, k)
    else:
        return select(A, q+1, length-1, k)


seed(42)

n = 10

for i in range(n):
    A = list(range(n))
    shuffle(A)
    # print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")