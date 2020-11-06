import random


def cw6():
    t = 1000
    list_ = [random.randint(1, 1000) for i in range(t)]
    for i in range(t):
        number = list_[i]
        n = False
        if number > 0:
            if number % 2 == 1:
                n = True
            number //= 10
        if n == False:
            return False
    return True


if __name__ == '__main__':
    print(cw6())
