# Jakub Radek
# Program ten spisuje zawartość tablicy 2d do tablicy 1d, którą sortuje przy pomocy algorytmu quicksort, a następnie
# nadpisuje elementy tablicy 2d odpowiednimi pozycjami z tablicy 1d, wiedząc że tablica 1d będzie miała 3 części, te które
# mają być poniżej przekąnej, te które mają nią być i te które mają być ponadnią, w tej kolejności
# Szacowana złożoność tego algorytmu to n^2logn


from zad1testy import runtests


def quicksort(A, first_i, last_i):
    if first_i < last_i - 1:
        pivot = A[last_i - 1]
        empty = first_i
        for i in range(first_i, last_i - 1):
            if A[i] < pivot:
                A[empty], A[i] = A[i], A[empty]
                empty += 1
        A[empty], A[last_i - 1] = A[last_i - 1], A[empty]
        A = quicksort(A, first_i, empty)
        A = quicksort(A, empty + 1, last_i)
        return A
    else:
        return A


def Median(T):
    n = len(T)
    array = []
    for _ in T:
        array += _

    array = quicksort(array, 0, n * n)
    median_pos = ((n * n - n) // 2)
    for i in range(n):
        T[i][i] = array[i + median_pos]
        for j in range(i + 1, n):
            T[j][i] = array[i + j - 1]
            T[i][j] = array[median_pos + n + j - 1]
    return T


runtests(Median)
