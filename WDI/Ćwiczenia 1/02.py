if __name__ == '__main__':

    a = 0
    b = 1
    c = 1010
    d = 1010

    while a < 1011:
        x = a
        y = b
        while y <= 2020:
            if y == 2020:
                if c+d > a+b:
                    c = a
                    d = b
            y = y + x
            x = y - x
        if b < 1010:
            b += 1
        else:
            a += 1
            b = a
    print(c, d, c+d)
