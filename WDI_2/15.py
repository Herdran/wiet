if __name__ == '__main__':
    number = 1
    while number < 100000:
        n = number
        sum_ = 0
        length = 0
        while number // (10**length) > 0:
            length += 1
        while n > 0:
            sum_ += (((number // 10**(n-1))-((number // 10**n)*10))**length)
            n -= 1
        if sum_ == number:
            print("da number:", number)
        number += 1
