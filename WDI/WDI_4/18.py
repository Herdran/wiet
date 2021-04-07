import random


def cw17(n, list_):
    vertical_max = 0
    horizontal_max = 0
    for i in range(n):
        for j in range(n):
            vertical = 0
            horizontal = 0
            print(list_[i][j])
            for a in range(i, n):
                if a + 1 > 10:
                    break
                vertical += list_[a][j]
            for b in range(j, n):
                if b + 1 > 10:
                    break
                horizontal += list_[i][b]
            print(vertical, horizontal)
            if vertical > vertical_max:
                vertical_max = vertical
            if horizontal > horizontal_max:
                horizontal_max = horizontal

    return max(vertical_max, horizontal_max)


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
