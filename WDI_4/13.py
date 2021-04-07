def if_prime_number(list_):
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
    i = 0
    for i in range(len(list_)):
        if list_[i] in list_of_primes:
            return True
    return False


def cw13(n, list_):
    for i in range(n):
        for j in range(n):
            list2_ = [0] * (n * n - 1)
            z = 0
            for x in range(n):
                for y in range(n):
                    if x != i or y != j:
                        if list_[x][y] == 0:
                            list2_[z] = 0
                        else:
                            list2_[z] = list_[i][j] + list_[x][y]
                        z += 1
            if if_prime_number(list2_) == False:
                list_[i][j] = 0

            # print(list2_)
    print(list_)

if __name__ == '__main__':
    n = 4
    # list_ = [[0] * n for i in range(n)]

    list_ = [1, 3, 1, 1], [1, 1, 5, 1], [1, 1, 1, 1], [1, 1, 1, 1]
    list2_ = [0] * (n * n)
    print(cw13(n, list_))

    # for i in list_:
    #     print(i)
