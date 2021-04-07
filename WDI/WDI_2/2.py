if __name__ == '__main__':
    a = 4
    b = 3
    n = 100
    print(a // b, end="")
    a = a % b
    print(".", end="")
    while n > 0:
        a *= 10
        print(a // b, end="")
        a = a % b
        n -= 1
