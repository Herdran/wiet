import random


def cw10():
    t = 1000
    list_ = [random.randint(1, 1000) for _ in range(t)]
    list2_ = []
    list3_ = []
    x = 0

    print(list_)
    while x < t - 1:
        i = x
        list2_.append(list_[i])
        r = list_[i + 1] - list_[i]
        while i < t - 1:
            i += 1
            print(list2_, r, i, x)
            if list_[i] == list_[i-1] + r:
                list2_.append(list_[i])
            if list_[i] != list_[i - 1] + r or i == t - 1:
                if len(list2_) > len(list3_):
                    list3_.clear()
                    for j in range(len(list2_)):
                        list3_.append(list2_[j])
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
    return list3_


if __name__ == '__main__':
    print(cw10())
