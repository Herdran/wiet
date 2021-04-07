"""Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool."""


def number_weight(n):
    weight = 0
    i = 2
    add_weight = False
    while n > 1:
        while n % i == 0:
            n //= i
            add_weight = True
        if add_weight == True:
            weight += 1
            add_weight = False
        i += 1
    return weight


def cw_02(t):
    length = len(t)
    list_ = [0] * length
    for i in range(length):
        list_[i] = number_weight(t[i])
    sum_ = sum(list_)
    first_sum = 0
    print(list_)
    if sum_ % 3 == 0:
        for i in range(length):
            first_sum += list_[i]
            second_sum = 0
            for j in range(i + 1, length):
                second_sum += list_[j]
                if second_sum == first_sum and sum_ - 3 * first_sum == 0:
                    return True
                if second_sum > first_sum:
                    break
    return False


if __name__ == '__main__':
    # print(number_weight(1))
    list_ = [64, 6, 30, 30]
    print(cw_02(list_))
