if __name__ == '__main__':
    number = int(input("A namber: "))
    length = 0
    while number // (10**length) > 0:
        length += 1
    n = length
    while n > 0:
        if length == ((number // 10**(n-1))-((number // 10**n)*10)):
            print("jesss")
            n = -1
        else:
            n -= 1
    if n == 0:
        print("noł")