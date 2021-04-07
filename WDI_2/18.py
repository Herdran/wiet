def ciag_a(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return ciag_a(x-1) - ciag_b(x-1) * ciag_a(x-2)


def ciag_b(x):
    if x == 0:
        return 2
    else:
        return ciag_b(x-1) + 2 * ciag_a(x-1)

if __name__ == '__main__':
    x = int(input("Input liczba: "))
    i = 0
    while x >= ciag_a(i): #a do dupy to i tyle
        if x == ciag_a(i):
            print(ciag_b(i))
            break
        i += 1
