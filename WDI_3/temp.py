import random


def kombinejszons(list_, list_of_combinations, x, length, y):
    z = y
    print(list_of_combinations, "jeeeej", length)
    for j in range(3):
        for i in range(length // 3 * j, (length // 3) * (j + 1)):
            list_of_combinations[i + z] += list_[x - z // 3]
            print(list_of_combinations, "wykonanie, yyyyyyyy", y)
            y = i
        x += 1
        if length // 3 > 0:
            kombinejszons(list_, list_of_combinations, x + 2, length // 3, y - 2)
    print(list_of_combinations, "testu", x)


def cw17():
    t = 2
    # list1_ = [random.randint(1, 1000) for _ in range(t)]
    # list2_ = [random.randint(1, 1000) for _ in range(t)]
    list1_ = [1, 2]
    list2_ = [3, 4]
    list3_ = []
    list_of_combinations = [0] * (3 ** t)
    sum_ = []
    for i in range(t):
        list3_.append(list1_[i])
        list3_.append(list2_[i])
        list3_.append(list1_[i] + list2_[i])

    list_of_combinationsss = kombinejszons(list3_, list_of_combinations, 0, len(list_of_combinations), 0)



if __name__ == '__main__':
    print(cw17())
