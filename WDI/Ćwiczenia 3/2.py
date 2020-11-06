if __name__ == '__main__':
    x = int(input("A cyfra: "))
    y = int(input("A cyfra tu: "))
    x_list = []
    y_list = []
    i = 0
    while x > 0:
        x_list.append(x % 10)
        x = x // 10
    while y > 0:
        y_list.append(y % 10)
        y = y // 10
    if len(x_list) == len(y_list) and len(x_list) > 0:
        while len(x_list) > 0 and i < len(x_list):
            if x_list[0] == y_list[i]:
                del x_list[0]
                del y_list[i]
                i = 0
            else:
                i += 1
        if x_list:
            print("nol")
        if not x_list:
            print("jesss")
    else:
        print("no")
