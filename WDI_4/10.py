import random


def cw10(n, list_):
    for i in range(n):
        x = 0
        for j in range(n):
            if list_[i][j] == 0:
                x = 1
            if j == n - 1 and x == 0:
                return False
    for j in range(n):
        x = 0
        for i in range(n):
            if list_[i][j] == 0:
                x = 1
            if i == n - 1 and x == 0:
                return False
    return True


if __name__ == '__main__':
    n = 4
    # list_ = [[0] * n for i in range(n)]

    list_ = [0, 2, 3, 4], [5, 0, 7, 8], [9, 10, 0, 0], [13, 14, 15, 16]

    # for i in range(n):
    #     list_[i][0] = random.randint(1, 10)
    #     for j in range(1, n):
    #         list_[i][j] = random.randint(list_[i][j - 1], 10)
    for i in list_:
        print(i)
    print(cw10(n, list_))
