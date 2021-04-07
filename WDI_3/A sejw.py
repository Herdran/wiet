import random


def kombinejszons(list_, list_of_combinations, x, length, y, dense):
    z = y
    if z < 0:
        z = 0
    print(length,"długieee", z)
    print(list_of_combinations, "jeeeej", length)
    for j in range(3):
        for i in range(length // 3 * j, (length // 3) * (j + 1)):
            print(y)
            list_of_combinations[i + z * ((dense + 1) // (len(list_) // 3))] += list_[x - z // 3 * ((dense + 1) // (len(list_) // 3))]
            y = i
            # print(list_of_combinations, "wykonanie, yyyyyyyy", x)
        x += 1
        if length // 3 > 0:
            kombinejszons(list_, list_of_combinations, x + 2, length // 3, y-2, dense + 1)
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

    list_of_combinationsss = kombinejszons(list3_, list_of_combinations, 0, len(list_of_combinations), 0, 0)



if __name__ == '__main__':
    print(cw17())
