from math import *


def bitonicTSP(C):
    def tspf(i, j, F, D):
        if F[i][j][0] != inf:
            return F[i][j]
        if i == j - 1:
            best = (inf, -1)
            for k in range(j - 1):
                best = min(best, (tspf(k, j - 1, F, D)[0] + D[k][j], k))
                # k oznacza tutaj indeks miasta w tablicy C na które przeszliśmy
            F[j - 1][j] = best
        else:
            F[i][j] = (tspf(i, j - 1, F, D)[0] + D[j - 1][j], -1)
        return F[i][j]

    # Sortuję tablicę C po wartościach współrzędnej x
    sorter = lambda x: (x[1])
    C = sorted(C, key=sorter)

    # Tworzę tablicę dystansu między miastami
    n = len(C)
    D = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            D[i][j] = sqrt((C[i][1] - C[j][1]) ** 2 + (C[i][2] - C[j][2]) ** 2)

    # Tworzę tablicę zawierającą minimalny koszt scieżek takich że ścieżki te odwiedzają każde miasto ze zbioru {1...i...j} dokładnie raz
    F = [[(inf, -1) for i in range(n)] for j in range(n)]
    # Algorytm jest identyczny jak ten prezentowany na wykładzie, z jedną różnicą, każdy element w tablicy F jest krotką,
    # poza kosztem ścieżki zawiera także miasto do którego mamy przejść, ale tylko wtedy gdy dochodzi do sytuacji i == j-1
    F[0][1] = (D[0][1], -1)

    # Wywołuję funkcję rekurencyjną
    for i in range(n - 1):
        tspf(i, n - 1, F, D)

    # Odczytuję wynik, gdzie i to indeks miasta na ścieżce secondary
    x = (inf, -1)
    for i in range(n):
        if x[0] > F[i][n - 1][0] + D[i][n - 1]:
            x = (F[i][n - 1][0] + D[i][n - 1], i)
    # Zapisuję wynik długości najkrótszej ścieżki, na wypadek gdyby algorytm miał ją również zwrócić
    distance = x[0]

    # Tablica primary zaczyna od elementu n-1, tablica secondary od x[1], czyli i
    primary_list = []
    secondary_list = []

    # Zapisuję indeksy elementów na których operuję
    primary = n - 1
    secondary = x[1]

    # Tak długo jak różnica między primary i secondary jest większa niż 1, to wiemy że elementy o indeksie
    # secondary<index<primary należą do tej samej ścieżki, u mnie jest to zawsze primary
    # Gdy dochodzi do sytuacji, że primary = secondary + 1, odczytuję wartość F[secondary][primary][1], która będzie indeksem miasta
    # do którego kontynuowana jest ścieżka primary, następnie zamieniam primary i primary_list miejscami z secondary i secondary_list
    # dzięki czemu mogę ponownie spisać wszystkie elementy o indeksie secondary<index<primary jako część tej samej ścieżki, primary,
    # ale będzie to już ta druga ścieżka niż poprzednio. Cykl powtarza się tak długo jak wartość primary nie osiągnie zera
    # tablice primary_list i secondary_list będą zawierały ścieżki od elementu n-1 do 0 a także od x[1] do 0, bez elementu
    # zerowego
    while primary != 0:
        if primary != secondary + 1:
            primary_list.append(primary)
            primary -= 1
        else:
            primary_list.append(primary)
            primary = F[secondary][primary][1]
            primary, secondary = secondary, primary
            primary_list, secondary_list = secondary_list, primary_list
    # ręcznie wypisuję element zerowy na początku i końcu, ponieważ wiem że musi tam wystąpić
    print(C[0][0], end=", ")
    # Wypisuję miasta z tablicy C o indeksach z tablicy secondary_list od końca, następnie z primary_list w normalnej kolejności
    for _ in range(len(secondary_list) - 1, -1, -1):
        print(C[secondary_list[_]][0], end=", ")
    for _ in range(len(primary_list)):
        print(C[primary_list[_]][0], end=", ")
    print(C[0][0])

    print(distance)
# C = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
# C = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
#      ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
#      ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]
# bitonicTSP(C)
