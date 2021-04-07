import random


def cw12():
    t = 100
    list_ = [random.randint(1, 99) for _ in range(t)]
    list2_ = []
    list3_ = []
    list4_ = []
    x = 0

    print(list_)
    while x < t - 1:
        i = x
        list2_.append(list_[i])
        r = list_[i + 1] - list_[i]
        while i < t - 1:
            i += 1
            if list_[i] == list_[i - 1] + r:
                list2_.append(list_[i])
                print(list2_)
            if list_[i] != list_[i - 1] + r or i == t - 1:
                if len(list2_) > len(list3_) and r > 0:
                    list3_.clear()
                    for j in range(len(list2_)):
                        list3_.append(list2_[j])
                    list2_.clear()
                    list2_.append(list_[i])
                    if i < t - 1:
                        r = list_[i + 1] - list_[i]
                elif len(list2_) > len(list4_) and r < 0:
                    list4_.clear()
                    for j in range(len(list2_)):
                        list4_.append(list2_[j])
                    list2_.clear()
                    list2_.append(list_[i])
                    if i < t - 1:
                        r = list_[i + 1] - list_[i]
                else:
                    list2_.clear()
                    list2_.append(list_[i])
                    if i < t - 1:
                        r = list_[i + 1] - list_[i]
        x += 1
        list2_.clear()
    return list3_, list4_, len(list3_) - len(list4_)


if __name__ == '__main__':
    print(cw12())
