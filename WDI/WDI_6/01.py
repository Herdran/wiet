"""Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfry"""


def prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    a = 5
    while a <= (n**(1/2)):
        if n % a == 0:
            return False
        a += 2
        if n % a == 0:
            return False
        a += 4
    return True


def cw_01(n, y):
    x = n
    length = 0
    while x > 0:
        length += 1
        x //= 10
    for i in range(length):
        x = n
        temp = (x // (10**i)) - (x // 10 ** (i + 1))
        # print(x, temp)
        # print((x // (10**i)), (x // 10 ** (i + 1)))
        x -= temp * 10**i
        # print(x, temp)
        if prime(x) == True and x not in y:
            # print(x)
            y.add(x)
        if length > 3:
            cw_01(x, y)
    return y


if __name__ == '__main__':
    y = set()
    print(cw_01(978896667, y))
