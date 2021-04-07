if __name__ == '__main__':
    number = int(input("A namber: "))
    length = 0
    while number // (10**length) > 0:
        length += 1
    if length == 1:
        length = -1
        print("Pojedyncza liczba jes")
    while length > 1:
        if ((number // 10**(length-1))-((number // 10**length)*10)) >= (number // 10 ** (length - 2) - ((number // 10**(length-1)) * 10)):
            print("ne rosnie")
            length = 0
        else:
            length -= 1
    if length == 1:
        print("rosnie")
