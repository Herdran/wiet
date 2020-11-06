def palindrom_tf(number):
    x = number
    y = 0
    while x > 0:
        y *= 10
        y += x % 10
        x = x // 10
    if y == number:
        return True
    else:
        return False


def palindrom(number):
    x = number
    y = 0
    while x > 0:
        y *= 10
        y += x % 10
        x = x // 10
    return(y)


def my_bin(number):
    x = number
    y = 2
    while x > 0:
        y *= 10
        y += x % 2
        x = x // 2
    y = palindrom(y)
    y -= 2
    y = y // 10
    return y


def palindrom_bin_tf(number):
    x = number
    y = 2
    while x > 0:
        y *= 10
        y += x%2
        x = x//2
    z = y
    y = palindrom(y)
    y -= 2
    y = y // 10
    if y == z:
        return True
    else:
        return False


if __name__ == '__main__':
    print(palindrom(121))
    print(palindrom_tf(121))
    print(my_bin(7))
    print(palindrom_bin_tf(7))
