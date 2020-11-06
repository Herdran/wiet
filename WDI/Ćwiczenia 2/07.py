if __name__ == '__main__':
    number = int(input("A namber: "))
    n = 1
    while number > n:
        if number % (n*n+n+1) == 0:
            print("jes")
        n += 1
