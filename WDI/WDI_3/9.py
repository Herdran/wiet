import random


def cw9():
    t = 1000
    list_ = [random.randint(1, 1000) for i in range(t)]
    list2_ = []
    list3_ = []
    i = 1
    list2_.append(list_[0])
    print(list_)
    while i < t:
        if list_[i] > list_[i-1]:
            list2_.append(list_[i])
        print(list2_)
        if list_[i] <= list_[i-1]:
            if len(list2_) > len(list3_):
                list3_.clear()
                for j in range(len(list2_)):
                    list3_.append(list2_[j])
                list2_.clear()
                list2_.append(list_[i])
            else:
                list2_.clear()
                list2_.append(list_[i])
        i += 1
    return list3_






if __name__ == '__main__':
    print(cw9())
    # print(if_prime_number(23))
