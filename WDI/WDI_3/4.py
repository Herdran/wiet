if __name__ == '__main__':
    n = 10000
    x = 0
    sum_ = [0] * n
    temp = [1] * n
    while temp != sum_:
        for i in range(n):
            temp[i] = sum_[i]
        factorial = 1
        for i in range(1, x+1):
            factorial *= i
        factorial = 1/factorial
        j = 0
        while factorial > 0 and j < n-1:
            if factorial > 10:
                factorial /= 10
            if factorial < 1:
                factorial *= 10
                j += 1
            if 1 <= factorial < 10:
                sum_[j] += int(factorial // 1)
                factorial = (factorial - (factorial // 1)) * 10
                j += 1
        for i in range(1, n):
            if sum_[i] > 9:
                sum_[i] -= 10
                sum_[i-1] += 1
        x += 1
    del sum_[0]
    print(2, ".", *sum_, sep="")
