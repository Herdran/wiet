def if_prime_number_inside(x):
    list_ = []
    while x > 0:
        list_.append(x % 10)
        x //= 10
    n = max(list_)
    j = 0
    list_of_primes = [i for i in range(2, n + 1)]
    # print(n, list2_)
    while j <= len(list_of_primes):
        for i in range(j + 1, len(list_of_primes)):
            if list_of_primes[i] % list_of_primes[j] == 0:
                list_of_primes[i] = 0
        x = list_of_primes.count(0)
        for i in range(x):
            list_of_primes.remove(0)
        j += 1
    for i in range(len(list_)):
        if list_[i] in list_of_primes:
            return True
    return False

def cw15(n, list_):
    for i in range(n):
        z = False
        for j in range(n):
            z = if_prime_number_inside(list_[i][j])
            if z == False:
                break
        if z == True:
            return True
    return False


if __name__ == '__main__':
    n = 3
    # list_ = [[0] * n for i in range(n)]

    list_ = [1, 3, 1], [3, 3, 5], [1, 1, 1]
    print(cw15(n, list_))

    # for i in list_:
    #     print(i)
