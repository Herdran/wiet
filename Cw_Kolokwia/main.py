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
    # index_of_deleted.append(j)
    return list_combinations

if __name__ == '__main__':
    list1_ = [1, 2, 3, 4, 5]
    sum_ = 15
    z = 1
    list_combinations = []
    print(deleting(list1_, sum_, list_combinations, 5, z + 1, []))
    # print(powt(list1_, list2_))
