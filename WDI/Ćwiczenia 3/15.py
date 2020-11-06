import random


def if_fibonacci(z):
    x = 0
    y = 1
    while x <= 1000000:
        if x == z:
            return True
        y = y + x
        x = y - x
    return False


def if_prime_number(z):
    n = 1000
    x = 0
    j = 0
    list_ = [i for i in range(2, n + 1)]
    while j <= len(list_):
        for i in range(j + 1, len(list_)):
            if list_[i] % list_[j] == 0:
                list_[i] = 0
        x = list_.count(0)
        for i in range(x):
            list_.remove(0)
        j += 1
    i = 0
    while list_[i] <= z:
        if list_[i] == z:
            return True
        i += 1
    return False


def cw15():
    t = 10
    n = False
    list_ = [random.randint(1, 1000) for _ in range(t)]
    print(list_)
    for i in range(t):
        if if_fibonacci(i):
            print("fibo", i)
            if if_prime_number(list_[i]) or list_[i] == 1:
                print("nooo")
                return False
        else:
            if if_prime_number(list_[i]):
                n = True
    return n


if __name__ == '__main__':
    print(cw15())
