"""Zadanie 2. Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
o 2 niewiadomych."""


def create():
    l, m = (input("Input: ").split())
    return int(l), int(m)


def output(n):
    if n[1] < 0:
        print(f"({n[0]}x{n[1]}y={n[2]})")
    else:
        print(f"({n[0]}x+{n[1]}y={n[2]})")


def addition(a, b):
    return a[0] * b[1] + a[1] * b[0], a[1] * b[1]


def substraction(a, b):
    return a[0] * b[1] - a[1] * b[0], a[1] * b[1]


def multiplication(a, b):
    return a[0] * b[0], a[1] * b[1]


def division(a, b):
    return a[0] * b[1], a[1] * b[0]


def exponentiation(a, n):
    return a[0] ** n, a[1] ** n


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


def w(eq):
    return substraction(multiplication(eq[0][0], eq[1][1]), multiplication(eq[0][1], eq[1][0]))


def wx(eq):
    return substraction(multiplication(eq[0][2], eq[1][1]), multiplication(eq[0][1], eq[1][2]))


def wy(eq):
    return substraction(multiplication(eq[0][0], eq[1][2]), multiplication(eq[0][2], eq[1][0]))

def solve(eq):
    w_ = w(eq)
    wx_ = wx(eq)
    wy_ = wy(eq)

    if w_ == 0:
        if wx_ == wy_ == 0:
            return "nieoznaczone"
        return "sprzeczne"

    return reduction(division(wx_, w_)), reduction(division(wy_, w_))


if __name__ == '__main__':
    # a = create()
    # b = create()
    # a = (2, 3, 7)
    # b = (5, -8, 2)
    # a = (2, 1)
    # b = (3, 1)
    # c = (7, 1)
    # d = (5, 1)
    # e = (-8, 1)
    # f = (2, 1)
    a = (1, 2)
    b = (1, 3)
    c = (1, 4)
    d = (1, 5)
    e = (1, 6)
    f = (1, 7)
    eq = [[a, b, c], [d, e, f]]
    # print(w(eq))
    # print(wx(eq))
    # print(wy(eq))
    print(solve(eq))
    # output(a)
    # output(b)
    # print(main_determinant_of_two(a, b))
    # print(addition(a, b))
    # print(substraction(a, b))
    # print(multiplication(a, b))
    # print(division(a, b))
    # print(exponentiation(a, 2))
    # print(reduction(a))
