if __name__ == '__main__':
    list_ = []
    x = 1
    while x != 0:
        x = int(input("Namber: "))
        list_.append(x)
    list_.remove(0)

    for i in range(len(list_)):
        for j in range(len(list_)):
            if list_[i] < list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    print(list_)
    if len(list_) >= 10:
        print(list_[9])
    else:
        print(list_[-1])
