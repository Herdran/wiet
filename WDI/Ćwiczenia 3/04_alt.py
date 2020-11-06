if __name__ == '__main__':
    n = 1000
    factorial = 1
    sum_ = 1 * (10 ** n)
    temp = 0
    i = 1
    while sum_ != temp:
        temp = sum_
        factorial *= i
        i += 1
        denominator = (10 ** n // factorial)
        sum_ += denominator
    temp = sum_ // 10**n
    sum_ -= temp * (10 ** n)
    print(temp ,".", sum_, sep="")
