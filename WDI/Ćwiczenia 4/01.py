if __name__ == '__main__':
    n = 10
    list_ = [[0] * n for i in range(n)]
    print(list_)
    i = 0
    j = 0
    x = 1
    y = 0
    list_[0][0] = x

    while y < n / 2:
        while j < n - 1 - y:
            x += 1
            j += 1
            list_[i][j] = x
        while i < n - 1 - y:
            x += 1
            i += 1
            list_[i][j] = x
        while j > 0 + y:
            x += 1
            j -= 1
            list_[i][j] = x
        while i > 0 + 1 + y:
            x += 1
            i -= 1
            list_[i][j] = x
        y += 1

    # for i in range(n):
    #     print("[", end="")
    #     for j in range(n):
    #         print(list_[i][j], end="")
    #         if j < n-1:
    #             print(",", end="")
    #         else:
    #             print("]")
    #  I may be retarded

    for i in list_:
        print(i)
