def cw_11(i, sum_):
    if i == N:
        if sum_ == enka:
            return 1
        return 0

    return cw_11(i + 1, sum_ * arr[i]) + cw_11(i + 1, sum_)



N = 5
arr = [1, 3, 1, 6, 2]
enka = 6
print(cw_11(0, 1))
