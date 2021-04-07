import random

# q = list_[y + 1][y + 1] / list_[y][y]
# for i in range(y + 1, n - 1):
#     quotient = list_[i + 1 + y + j][i + 1 + y - j] / list_[i][i]
#     if q != quotient:
#         i = n
#     elif i == n - 2:
#         print("jeeeeej", q)
#         return True

dobra jebać to




def cw8(n, list_, y):
    z = 1
    q = 0
    a = 1
    b = 0
    for y in range(1 + (n-3) * 2):
        for j in range(z):
            c = 1
            for i in range(n - y - 1):
                print(i)
                quotient = list_[i + 1 + (z - 1) * c + y // 2][i + 1 + (z - 1) * (-1 * c) + y // 2] / list_[i + (z - 1) * c + y // 2][i + (z - 1) * (-1 * c) + y // 2]
                print("waaaaj", quotient, i + (z - 1) * c + y // 2, i + (z - 1) * (-1 * c) + y // 2)

                print(i + 1 + (z - 1) ** (c - 1) + y // 2, i + 1 + (z - 1) ** (c) + y // 2)
                if q == quotient or q == 0:
                    a += 1
                    q = quotient
                else:
                    break
            if c == 1:
                c = 0
            else:
                c = 1
            if a == n - y:
                return a
            if a >= 3:
                b = a
            a = 1
            q = 0


        if y < (n-3) * 2 - 1:
            z += 1
        else:
            z -= 1
        # print(z)


if __name__ == '__main__':
    n = 4
    # list_ = [[0] * n for i in range(n)]

    list_ = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 36, 12], [13, 14, 15, 26]

    list2_ = [0] * (n * n)
    # for i in range(n):
    #     list_[i][0] = random.randint(1, 10)
    #     for j in range(1, n):
    #         list_[i][j] = random.randint(list_[i][j - 1], 10)
    for i in list_:
        print(i)

    print(cw8(n, list_, 0))
    list3_ = cw8(n, list_, list2_)
