if __name__ == '__main__':
    number = int(input("A namber: "))
    a = 2
    n = 1
    while number > n:
        if number % (3 * a + 1) == 0:
            print("jesss")
            n = number
        n += 1
        a = 3 * a + 1
