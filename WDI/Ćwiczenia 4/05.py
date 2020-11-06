import random


def quotient_of_rows(i, n, list_):
    x = 1
    for j in range(n):
        x *= list_[i][j]
    if x < 0:
        x *= -1
    return x


def quotient_of_columns(j, n, list_):
    y = 1
    for i in range(n):
        y *= list_[i][j]
    if y < 0:
        y *= -1
    return y


def cw5(n, list_):
    a = 1
    b = 1
    for i in range(n):
        for j in range(n):
            x = quotient_of_rows(i, n, list_)
            y = quotient_of_columns(j, n, list_)

            if y / x > a / b:
                a = y
                b = x
                c = i
                d = j
    return c, d


if __name__ == '__main__':
    n = 3
    # list_ = [[random.randint(0, 10)] * n for i in range(n)]
    list_ = [37, 2, 2], [1, 2, 3], [11118333, 2, 4]
    print(list_)
    print(quotient_of_columns(1, 3, list_))
    print(cw5(n, list_))
