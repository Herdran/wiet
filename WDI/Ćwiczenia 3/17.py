import random

#prosze mnie nie bulić za tego potworka, działa
def filter_non_prime_numbers(list_of_combinations):
    n = 1
    j = 0
    for i in range(len(list_of_combinations)):
        if n < list_of_combinations[i]:
            n = list_of_combinations[i]

    list_ = [i for i in range(2, n + 1)]
    while j <= len(list_):
        for i in range(j + 1, len(list_)):
            if list_[i] % list_[j] == 0:
                list_[i] = 0
        x = list_.count(0)
        for i in range(x):
            list_.remove(0)
        j += 1

    for i in range(len(list_of_combinations)):
        x = list_of_combinations[i]
        if x not in list_:
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
                shift += 1
            shift -= 1
            x += 1
        x -= 3
    if y < dense:
        kombinejszons(list_, list_of_combinations, x + 3, length, y + 1, dense)
    return list_of_combinations


def cw17():
    t = 2
    # list1_ = [random.randint(1, 1000) for _ in range(t)]
    # list2_ = [random.randint(1, 1000) for _ in range(t)]
    # nie umiem pisac randint I guess
    list1_ = [1, 2]
    list2_ = [3, 4]
    list3_ = []
    list_of_combinations = [0] * (3 ** t)
    sum_ = []
    for i in range(t):
        list3_.append(list1_[i])
        list3_.append(list2_[i])
        list3_.append(list1_[i] + list2_[i])

    list_ = (kombinejszons(list3_, list_of_combinations, 0, len(list_of_combinations), 1, t))
    print(filter_non_prime_numbers(list_))


if __name__ == '__main__':
    print(cw17())
