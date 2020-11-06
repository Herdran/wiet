import random


def cw16():
    t = 10
    list_ = [random.randint(1, 1000) for _ in range(t)]
    min_, max_ = list_[0], list_[0]
    print(list_)
    for i in range(1, t):
        if list_[i] > max_:
            max_ = list_[i]
        if list_[i] < min_:
            max_ = list_[i]
    list_.remove(max_)
    list_.remove(min_)
    for i in range(1, t - 2):
        if list_[i] == max_:
            return False
        if list_[i] == min_:
            return False
    return True


if __name__ == '__main__':
    print(cw16())
