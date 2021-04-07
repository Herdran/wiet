def deleting(list_, sum_, list_combinations, n, a, index_of_deleted):
    for j in range(n):
        if j not in index_of_deleted:
            sum_ -= list_[j]
            index_of_deleted.append(j)
            if a < n:
                deleting(list_, sum_, list_combinations, n, a + 1, index_of_deleted)
            if a == n:
                list_combinations.append(sum_)
            index_of_deleted.remove(j)
            sum_ += list_[j]
    return list_combinations


def funkcja(list1_, list2_):
    n = len(list1_)
    amount = n
    z = n - 1
    x = 0
    y = 0
    list_combinations_1 = []
    list_combinations_2 = []
    while amount > 0:
        for i in range(z, n):

            for j in range(n):
                x += list1_[j]
                y += list2_[j]
            if amount < n:
                list_combinations_1 = (list1_, x, list_combinations_1, n, z + 1, [])
                list_combinations_2 = (list2_, x, list_combinations_2, n, z + 1, [])
            else:
                list_combinations_1.append(x)
                list_combinations_2.append(y)

        for a in range(len(list_combinations_1)):
            if list_combinations_1[a] in list_combinations_2:
                return amount
        list_combinations_1.clear()
        list_combinations_2.clear()
        amount -= 1
        z -= 1
        x = 0
        y = 0
    return "no"


if __name__ == '__main__':
    # n = 5
    list1_ = [1, 2, 3, 3, 5]
    list2_ = [1, 2, 3, 4, 6]
    print(funkcja(list1_, list2_))
