if __name__ == '__main__':
    number = int(input("A namber: "))
    n = 2
    a, b = number, number
    while n < number:
        if number % n == 0:
            if a + b > n + number / n:
                a = n
                b = number // n
        n += 1
    print(number, "is an iloczyn of", a, b)
