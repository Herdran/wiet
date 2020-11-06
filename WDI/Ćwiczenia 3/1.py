def exchange(x, y):
    list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    number = []

    while x > 0:
        number.append(list_[x % y])
        x = x // y
    # i = 0
    # while x > 0:
    #     number[i] = (list_[x % y])
    #     x = x // y
    #     i += 1
    number.reverse()
    print(*number, sep="")


if __name__ == '__main__':
    y = int(input("A system: "))
    x = int(input("A number: "))
    exchange(x, y)
