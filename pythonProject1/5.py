def shopping():
    with open("data.txt") as data:
        to_buy = data.readline()
        to_buy = to_buy[:-1]
        list_to_buy = to_buy.split(', ')
        data.readline()
        can_buy = []
        for line in data:
            can_buy.extend(line[:-1].split(', '))

        for item in list_to_buy:
            if item in can_buy:
                list_to_buy.remove(item)
        if not list_to_buy:
            print('ok')
        else:
            print(list_to_buy)


if __name__ == "__main__":
    shopping()