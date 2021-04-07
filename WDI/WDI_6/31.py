"""Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów elementów
wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać podzielniki do
tablicy pomocniczej. Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
"""
from time import time
start_time = time()


def factorize(n):
    factors = []
    i = 2
    while n > 1:
        add_ = False
        while n % i == 0:
            add_ = True
            n //= i
        if add_:
            factors.append(i)
        i += 1
    return cw_31_alt(factors)
    return cw_31(factors)


def cw_31(list_, number=1, i=0):
    if i < len(list_):
        return cw_31(list_, number*list_[i], i+1) or \
               cw_31(list_, number*1, i+1)
    list_of_numbers.append(number)
    if list_of_numbers[-1] == 1:
        return sum(list_of_numbers[:-1])


def cw_31_alt(list_):
    sum_ = 1
    for i in list_:
        sum_ *= i+1
    return sum_ - 1


list_of_numbers = []
n = 2305567963945518424753102147331756070
print(factorize(n))
print(time()-start_time)

