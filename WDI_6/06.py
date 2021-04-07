"""Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba !10! bullshit może być 8."""


def cw_06(i=0, sum_=0, sum_id=0, len_=0):
    if i == N:
        if sum_ == sum_id and len_ != 0:
            return len_, sum_
        else:
            return N + 1, 0
    else:
        r1 = cw_06(i + 1, sum_ + arr[i], sum_id + i, len_ + 1)
        r2 = cw_06(i + 1, sum_, sum_id, len_)
        if r1[0] == r2[0]:
            if r1[1] < r2[1]:
                return r1
            else:
                return r2
        else:
            if r1[0] < r2[0]:
                return r1
            else:
                return r2


arr = [1, 7, 3, 5, 11, 2]
N = 6
print(cw_06())
