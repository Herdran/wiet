"""Zadanie 4. Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy
ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG."""


def create():
    l, m = (input("Input: ").split())
    return int(l), int(m)


def output(n):
    print(f"({n[0]}/{n[1]})")


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
    if b == 0:
        return a
    return gcd(b, a % b)


def reduction(a):
    x = gcd(a[0], a[1])
    a = a[0] / x, a[1] / x
    return int(a[0]), int(a[1])


def check_sequences(list_):
    arithmetic = 0
    geometric = 0
    for i in range(len(list_) - 1):
        length_arithmetic = 1
        length_geometric = 1
        end_a = False
        end_g = False
        starting_r = substraction(list_[i + 1], list_[i])
        starting_q = reduction(division(list_[i + 1], list_[i]))
        for j in range(i, len(list_) - 1):
            r = substraction(list_[j + 1], list_[j])
            q = reduction(division(list_[j + 1], list_[j]))
            if length_arithmetic >= 2 and r == starting_r and end_a == False:
                arithmetic += 1
            if length_arithmetic >= 2 and r != starting_r:
                end_a = True
            if r == starting_r:
                length_arithmetic += 1
            if length_geometric >= 2 and q == starting_q and end_g == False:
                geometric += 1
            if length_geometric >= 2 and q != starting_q:
                end_g = True
            if q == starting_q:
                length_geometric += 1

    print(arithmetic, geometric)
    if arithmetic > geometric:
        return 1
    if arithmetic < geometric:
        return -1
    return 0


if __name__ == '__main__':
    # list_ = [(2, 1), (4, 1), (8, 1), (10, 1), (100, 8)]
    list_ = [(1, 1), (2, 1), (3, 1), (4, 1), (2, 1), (3, 1), (4, 1), (16, 3)]
    print(check_sequences(list_))