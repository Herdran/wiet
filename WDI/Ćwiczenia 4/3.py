import random


def is_any_number_even(x):
    while x > 0:
        if x % 2 == 0:
            return True
        x //= 10
    return False


def cw3(n, list_):
    for i in range(n):
        for j in range(n):
            x = list_[i][j]
            x = is_any_number_even(x)
            if x == False:
                break
            if x == True and j == n - 1:
                return True
    return False


if __name__ == '__main__':
    n = 3
    # list_ = [[random.randint(0, 10)] * n for i in range(n)]
    list_ = [37, 2, 2], [1, 2, 3], [11118333, 2, 4]
    print(list_)
    print(cw3(n, list_))
