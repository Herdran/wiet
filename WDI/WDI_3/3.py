if __name__ == '__main__':
    n = 1000
    x = 0
    j = 0
    list_ =[i for i in range(2, n+1)]
    while j <= len(list_):
        for i in range(j+1, len(list_)):
            if list_[i] % list_[j] == 0:
                list_[i] = 0
        x = list_.count(0)
        for i in range(x):
            list_.remove(0)
        j += 1
    print(*list_, sep=",")
