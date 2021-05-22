# Jakub Radek
# Algorytm najpierw konsoliduje całą ropę w pojedyńczych plamach w 0 wierszu, najbliżej indeksowi 0 jak się da, dzięki
# temu wiersz 0 tablicy T ma w sobie całą ropę do jakiej będziemy mieć dostęp na pozycjach na których najwcześniej będziemy
# mogli ją zebrać. Następnie wyruszamy, jeśli stoimy na polu z ropą to dodajemy ilość ropy i indeks pola do kolejki priorytetowej,
# kiedy poziom paliwa wynosi 0, to ściągamy z kolejki priorytetowej największą ilośc ropy i tankujemy "retroaktywnie", nadpisując indeks na
# którym była wartością -1, dla odczytu później. Gdy dotrzemy na miejsce przechodzi ponownie po 0 wierszu tablicy i appendujemy
# do osobnej tablicy indeksy na których się zatrzymaliśmy. Szacowana złożoność tego algorytmu to O(length*depth), czyli iloczyn
# rozmiarów tablicy


# from zad3testy import runtests
from queue import PriorityQueue


def plan(T):
    def collect(T, x, y, depth, length):
        value = T[x][y]
        T[x][y] = 0

        for i, j in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if 0 <= i < depth and 0 <= j < length and T[i][j] > 0:
                value += collect(T, i, j, depth, length)

        return value

    length = len(T[0])
    depth = len(T)
    for i in range(length):
        if T[0][i] > 0:
            T[0][i] = collect(T, 0, i, depth, length)

    Q = PriorityQueue()
    tank = 0
    position = 0
    while position < length-1:
        if T[0][position] != 0:
            Q.put([-T[0][position], position])
        if tank == 0:
            x = Q.get()
            tank -= x[0]
            T[0][x[1]] = -1
        position += 1
        tank -= 1

    answer = []
    for i in range(length):
        if T[0][i] == -1:
            answer.append(i)
    return answer


# runtests(plan)
