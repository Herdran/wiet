import random


def cw7():
    t = 1000
    list_ = [random.randint(1, 1000) for i in range(t)]
    for i in range(t):
        number = list_[i]
        n = False
        if number > 0:
            if number % 2 == 0:
                return False
            number //= 10
    return True


if __name__ == '__main__':
    print(cw7())
