import random


def cw13():
    t = 15
    # list_ = [random.randint(100, 999) for _ in range(t)]
    list_ = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
    list2_ = []
    list3_ = []
    x = 0
    r = 1
    y = t - 1
    length = 2

    print(list_)
    while x < t - 1:
        while length <= t - x:
            for j in range(x, length + x):
                list2_.append(list_[j])
            while y > 0 and y > length - 2:
                for j in range(length):
                    list3_.append(list_[y - j])
                print(list2_, list3_)
                if list2_ == list3_:
                    if r < len(list2_):
                        r = len(list2_)
                    y = 0
                    list2_.clear()
                    list3_.clear()
                y -= 1
                list3_.clear()
            list2_.clear()
            y = t - 1
            length += 1
        length = 2
        x += 1
    return r


if __name__ == '__main__':
    print(cw13())
