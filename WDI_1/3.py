if __name__ == '__main__':

    number = int(input("A sum: "))
    x = 0
    y = 1
    sum_ = 0
    a = 0
    b = 1
    while sum_ < number and x < 100000:
        if sum_ < number:
            sum_ += y
        y = y + x
        x = y - x
        while sum_ > number:
            sum_ -= b
            b = b + a
            a = b - a
    if sum_ == number:
        print("Jesss")
