def fibonacci(number):
    x = 0
    y = 1
    for i in range(number):
        y = y + x
        x = y - x
    return x


def fibonacci_alt(x, y, z):
    a = 1
    i = 1
    while a < (z*1)/4:
        x_f = x
        y_f = y
        a = fibonacci(i)
        while y_f < z:
            y_f = y_f + x_f
            x_f = y_f - x_f
            if z == y_f * a:
                return a, y_f
        i += 1


if __name__ == '__main__':
    z = int(input("A number: "))
    x = 0
    y = 1
    print(fibonacci_alt(x, y, z))
