def fibonacci(number):
    x = 0
    y = 1
    for i in range(number):
        y = y + x
        x = y - x
    return x


if __name__ == '__main__':
    number = int(input("A namber: "))
    x = number+1
    sum_ = 0
    n = 1
    i = n
    while n < 1000:
        if sum_ < x:
            sum_ += fibonacci(i)
            i += 1
        if sum_ > x:
            sum_ = 0
            n += 1
            i = n
        if sum_ == x:
            x += 1
            sum_ = 0
            n = 1
            i = n
    print(x)
