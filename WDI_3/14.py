import random


def cw14():
    t = 20
    x = 100
    y = x
    n = 0
    list2_ = []
    while x > 0:
        list_ = [random.randint(1, 365) for _ in range(t)]
        # print(list_)
        for i in range(len(list_)):
            for j in range(i + 1, len(list_)):
                if list_[i] == list_[j] and list_[i] not in list2_:
                    list2_.append(list_[i])
                    # print(list_[i])
                    n += 1
        list2_.clear()
        x -= 1
    return (n*100) / (y * t)


if __name__ == '__main__':
    print(cw14())
