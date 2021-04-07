import random


def kombinejszons(list_, list_of_combinations, x, length, y, dense, z):
    sliding = 0
    for j in range(3):
        for i in range(length // 3 ** dense):
            list_of_combinations[i + j * length // 3 ** dense] += list_[x - y]
            print(list_of_combinations)

        z = i + j * length // (3 ** dense)
        # z = i + j * (z + 1)
        print(z, "zzzzzzz")
        input()
        if z - (length // (3 ** dense)) + 1 >= length // (3 ** dense):
            print("wadafak", z, length, dense)
            sliding = j * (z - (length // (3 ** dense)) + 1)
            print(sliding, "slajding")
        x += 1
        print(list_of_combinations, dense)
        if length // (3 ** dense) > 1:
            kombinejszons(list_, list_of_combinations, x + 2, length, j, dense + 1, z)



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

    list_of_combinationsss = kombinejszons(list3_, list_of_combinations, 0, len(list_of_combinations), 0, 1, 0)



if __name__ == '__main__':
    print(cw17())
