if __name__ == '__main__':
    number = 2
    while number < 1000000:
        n = number
        sum1_ = 0
        sum2_ = 0
        length = 0
        l = 0
        x = 2
        while number // (10 ** length) > 0:
            length += 1

        while length > 0:
            sum2_ += ((n // (10 ** (length - 1))) - ((n // 10 ** length) * 10))
            length -= 1

        while n > 1:
            while n % x != 0:
                x += 1
            if x == number:
                break
            if x < 10:
                sum1_ += x
            else:
                while x // (10 ** l) > 0:
                    l += 1
                while l > 0:
                    sum1_ += ((x // (10 ** (l - 1))) - ((x // 10 ** l) * 10))
                    l -= 1
            n /= x
        if sum1_ == sum2_:
            print(number, sum2_, "jesssss")
        number += 1
