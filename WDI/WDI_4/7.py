import random

def sortowanie(list_):
    for i in range(len(list_)):
        for j in range(i, len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    return list_



def cw7(n, list_, list2_):
    y = 0
    for i in range(n):
        for j in range(n):
            list2_[y] = list_[i][j]
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

    print(cw7(n, list_, list2_))
    list3_ = cw7(n, list_, list2_)
    print(sortowanie(list3_))
