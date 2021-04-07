import random


def cw11():
    t = 100
    list_ = [random.randint(1, 100) for _ in range(t)]
    list2_ = []
    list3_ = []
    x = 0
    while x < t - 1:
        i = x
        list2_.append(list_[i])
        q = list_[i + 1] / list_[i]
        while i < t - 1:
            i += 1
            if list_[i] == list_[i-1] * q:
                list2_.append(list_[i])
            if list_[i] != list_[i - 1] * q or i == t - 1:
                if len(list2_) > len(list3_):
                    list3_.clear()
                    for j in range(len(list2_)):
                        list3_.append(list2_[j])
                    list2_.clear()
                    list2_.append(list_[i])
                    if i < t - 1:
                        q = list_[i + 1] - list_[i]
                else:
                    list2_.clear()
                    list2_.append(list_[i])
                    if i < t - 1:
                        q = list_[i + 1] / list_[i]
        x += 1
        list2_.clear()
    if len(list3_) > 2:
        return list3_
    else:
        return "Noł ciag over tu"


if __name__ == '__main__':
    print(cw11())
