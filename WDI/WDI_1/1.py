if __name__ == '__main__':

    x = 0
    y = 1
    while x <= 1000000:
        print(x)
        y = y + x
        x = y - x
