import random


def cw9(n, list_, k):
    size = 3
    while size < n:
        for i in range(n - size + 1):
            for j in range(n - size + 1):
                x = list_[i][j] * list_[i + size - 1][j] * list_[i][size - 1 + j] * list_[i + size - 1][size - 1 + j]
                print("łaaaa", i, j, x)
                if x == k:
                    return f"There exists square with it's size being {size}, it's center is: ({(i + i + size - 1) // 2},{(j + j + size - 1) // 2})"
        size += 2
    return False


if __name__ == '__main__':
    n = 4
    # list_ = [[0] * n for i in range(n)]

    list_ = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]

    # for i in range(n):
    #     list_[i][0] = random.randint(1, 10)
    #     for j in range(1, n):
    #         list_[i][j] = random.randint(list_[i][j - 1], 10)
    for i in list_:
        print(i)
    print(cw9(n, list_, 107352))