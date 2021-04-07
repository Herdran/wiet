import random


def kombinejszons(list_, list_of_combinations, x, length, y):
    3 gęstości of recursion
    z = y
    print(z)
    print(list_of_combinations, "jeeeej", length)
    for j in range(3):
        for i in range(length // 3 * j, (length // 3) * (j + 1)):
            print(i, x)
            list_of_combinations[i + z] += list_[x - z // 3]
            print(list_of_combinations, "wykonanie, yyyyyyyy", y)
            y = i
        input()
        x += 1
        if length // 3 > 0:
            print("a testu", x)
            kombinejszons(list_, list_of_combinations, x + 2, length // 3, y - 2)
    print(list_of_combinations, "testu", x)


def cw17():
    t = 3
    # list1_ = [random.randint(1, 1000) for _ in range(t)]
    # list2_ = [random.randint(1, 1000) for _ in range(t)]
    list1_ = [1, 2, 3]
    list2_ = [4, 5, 6]
    list3_ = []
    list_of_combinations = [0] * (3 ** t)
    sum_ = []
    for i in range(t):
        list3_.append(list1_[i])
        list3_.append(list2_[i])
        list3_.append(list1_[i] + list2_[i])
    # print(list3_)
    list_of_combinationsss = kombinejszons(list3_, list_of_combinations, 0, len(list_of_combinations), 0)
    # print(list_of_combinations, len(list_of_combinations))
    #
    # print(len(list_of_combinations), len(list3_), "jess")
    #
    # for i in range(0, len(list_of_combinations), len(list3_)):
    #     for j in range(i+1, len(list3_) + i):
    #         print("oh jess")
    #         sum_.append(list_of_combinations[i]+list_of_combinations[j])
    # print(sum_, len(sum_))


if __name__ == '__main__':
    print(cw17())
