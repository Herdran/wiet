import random


def are_all_numbers_odd(x):
    while x > 0:
        if x % 2 == 0:
            return False
        x //= 10
    return True


def cw2(n, list_):
    for i in range(n):
        for j in range(n):
            x = list_[i][j]
            x = are_all_numbers_odd(x)
            if x == True:
                break
            if x == False and j == n - 1:
                return False
    return True


if __name__ == '__main__':
    n = 3
    # list_ = [[random.randint(0, 10)] * n for i in range(n)]
    list_ = [1, 2, 2], [1, 2, 3], [2, 2, 4]
    print(list_)
    print(cw2(n, list_))
