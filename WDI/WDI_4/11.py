import random

def comparison_of_numbers_components(x, y):
    z = max(x, y)
    n = 0
    while z > 0:
        n += 1
        z //= 10
    list_ = [0] * n
    list2_ = [0] * n
    for i in range(n):
        list_[i] = x // (10 ** (n - 1 - i)) - (x // (10 ** (n - i)) * 10)
        list2_[i] = y // (10 ** (n - 1 - i)) - (y // (10 ** (n - i)) * 10)

    for i in range(n):
        for j in range(i + 1, n):
            if list_[i] == list_[j]:
                list_[i] = 0
            if list2_[i] == list2_[j]:
                list2_[i] = 0

    z = list_.count(0) # tak możnaby to zrobić jako pętlę specjalnie dla Garka, nie chce mi się
    if z != list2_.count(0):
        return False

    for i in range(z):
        list_.remove(0)
        list2_.remove(0)

    for i in range(n - z):
        if not list_[i] in list2_ or not list2_[i] in list_:
            return False
    return True


def cw11(n, list_):
    z = 0
    for i in range(n):
        for j in range(n):
            x = list_[i][j]
            y = True
            if i < n - 1:
                y = comparison_of_numbers_components(x, list_[i + 1][j])
            if j < n - 1 and y == True:
                y = comparison_of_numbers_components(x, list_[i][j + 1])
            if 0 < i < n and y == True:
                y = comparison_of_numbers_components(x, list_[i - 1][j])
            if 0 < j < n and y == True:
                y = comparison_of_numbers_components(x, list_[i][j - 1])
            if y == True:
                z += 1
    return z

if __name__ == '__main__':
    n = 4
    # list_ = [[0] * n for i in range(n)]

    list_ = [12, 21, 3, 4], [12, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]

    list2_ = [0] * (n * n)
    # for i in range(n):
    #     list_[i][0] = random.randint(1, 100)
    #     for j in range(1, n):
    #         list_[i][j] = random.randint(1, 100)
    for i in list_:
        print(i)
    print(cw11(n, list_))

    # print(comparison_of_numbers_components(111523, 321))
