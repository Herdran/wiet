import random

# def sortowanie(list_):
#     for i in range(len(list_)):
#         for j in range(i, len(list_)):
#             if list_[i] > list_[j]:
#                 list_[i], list_[j] = list_[j], list_[i]
#     return list_


#  zmodyfikowane pod potrzeby zadania, czyli upośledzone ofc
def sortowanie(list_):
    for i in range(len(list_)):
        for j in range(i, len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    x = 0
    for i in range(len(list_)):
        if list_[i] == 0:
            x += 1
    for i in range(len(list_)):
        if x < len(list_):
            list_[i] = list_[x]
            x += 1
        else:
            list_[i] = 0
    return list_


def cw6(n, list_, list2_):
    y = 0
    for i in range(n):
        for j in range(n):
            x = list_[i][j]
            for a in range(n):
                for b in range(n):
                    if x < list_[a][b]:
                        b = n
                        break
                    if x == list_[a][b] and (a != i or b != j):
                        x = 0
                        a = n
                        b = n
                        break
            list2_[y] = x
            y += 1
    return list2_


if __name__ == '__main__':
    n = 3
    # list_ = [[0] * n for i in range(n)]

    list_ = [2, 7, 10], [9, 10, 10], [4, 4, 8]

    list2_ = [0] * (n * n)
    # for i in range(n):
    #     list_[i][0] = random.randint(1, 10)
    #     for j in range(1, n):
    #         list_[i][j] = random.randint(list_[i][j - 1], 10)
    for i in list_:
        print(i)

    print(cw6(n, list_, list2_))
    list3_ = cw6(n, list_, list2_)
    print(sortowanie(list3_))
