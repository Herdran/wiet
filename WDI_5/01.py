"""Zadanie 1. Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie"""


def create():
    l, m = (input("Input: ").split())
    return int(l), int(m)


def output(n):
    print(f"({n[0]}/{n[1]})")


def addition(a, b):
    return a[0]*b[1]+a[1]*b[0], a[1]*b[1]


def substraction(a, b):
    return a[0]*b[1]-a[1]*b[0], a[1]*b[1]


def multiplication(a, b):
    return a[0]*b[0], a[1]*b[1]


def division(a, b):
    return a[0]*b[1], a[1]*b[0]


def exponentiation(a, n):
    return a[0]**n, a[1]**n


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        b, a = a % b, b
        #end while
    return a
#end def

def reduction(a):
    x = gcd(a[0], a[1])
    a = a[0] / x, a[1] / x
    return int(a[0]), int(a[1])

if __name__ == '__main__':
    a = create()
    b = create()
    output(a)
    output(b)
    print(addition(a, b))
    print(substraction(a, b))
    print(multiplication(a, b))
    print(division(a, b))
    print(exponentiation(a, 2))
    print(reduction(a))

