import random


def filter_non_prime_numbers(list_of_combinations, sieve):
    for i in range(len(list_of_combinations)):
        x = list_of_combinations[i]
        if x not in sieve:
            x = 0
        list_of_combinations[i] = x

    x = list_of_combinations.count(0)
    for i in range(x):
        list_of_combinations.remove(0)
    return list_of_combinations


def kombinejszons(list_, list_of_combinations, x, length, y, dense):
    shift = 0
    for j in range(length // 3 ** y):
        for i in range(3):
            for z in range(3 ** (y - 1)):
                list_of_combinations[i + j * 3 + shift] += list_[x]
                # print(list_of_combinations)
                shift += 1
            shift -= 1
            x += 1
        x -= 3
    if y < dense:
        kombinejszons(list_, list_of_combinations, x + 3, length, y + 1, dense)
    return list_of_combinations


def cw17():
    t = 4
    # list1_ = [random.randint(1, 1000) for _ in range(t)]
    # list2_ = [random.randint(1, 1000) for _ in range(t)]
    list1_ = [1, 3, 2, 4]
    list2_ = [9, 7, 4, 8]
    list3_ = []
    list_of_combinations = [0] * (3 ** t)

    for i in range(t):
        list3_.append(list1_[i])
        list3_.append(list2_[i])
        list3_.append(list1_[i] + list2_[i])
    list_ = (kombinejszons(list3_, list_of_combinations, 0, len(list_of_combinations), 1, t))

    j = 0
    n = max(list_of_combinations) * 2
    sieve = [i for i in range(2, n + 1)]
    while j <= len(sieve):
        for i in range(j + 1, len(sieve)):
            if sieve[i] % sieve[j] == 0:
                sieve[i] = 0
        x = sieve.count(0)
        for i in range(x):
            sieve.remove(0)
        j += 1

    # print(list_)
    print(filter_non_prime_numbers(list_, sieve))


if __name__ == '__main__':
    cw17()
