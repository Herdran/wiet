"""Zadanie 2.
Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wyª¡cznie tablic¦ t, funkcja powinna zwróci¢
wartosc typu bool.
"""
from random import randint
from time import time
start_time = time()


def b22():
    def func(length, sum1=0, sum2=0, length1=0, length2=0, index=0):
        if length1 == length2 == length:
            if sum1 == sum2:
                return True
            return False
        else:
            if index < N:
                return func(length, sum1 + T[index], sum2, length1+1, length2, index+1) or \
                    func(length, sum1, sum2 + T[index], length1, length2+1, index+1) or \
                    func(length, sum1, sum2, length1, length2, index + 1)
    i = 1
    while i < N:
        if func(i):
            return True
        i += 1
    return False


N = 2
rr = (1, 10)
T = [1, 1]
# T = [randint(rr[0], rr[1]) for _ in range(N)]
print(b22())
print(time()-start_time)