import random


def cw17(n, list_):
    z = 0
    for i in range(n):
        for j in range(n):
            y = 0
            if i < n - 1:
                y += list_[i + 1][j]
            if j < n - 1:
                y += list_[i][j + 1]
            if 0 < i < n:
                y += list_[i - 1][j]
            if 0 < j < n:
                y += list_[i][j - 1]
            if y > z:
                z = y
                a = i
                b = j
    return z, a, b


if __name__ == '__main__':
    n = 4
    # list_ = [[0] * n for i in range(n)]

    list_ = [12, 21, 3, 4], [12, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]

    # for i in range(n):
    #     list_[i][0] = random.randint(1, 100)
    #     for j in range(1, n):
    #         list_[i][j] = random.randint(1, 100)
    for i in list_:
        print(i)
    print(cw17(n, list_))

    # print(comparison_of_numbers_components(111523, 321))
