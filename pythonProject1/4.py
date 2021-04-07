if __name__ == '__main__':

    with open("colors.txt") as data:
        list_ = data.read().split("\n")
        dict_ = {}
        for i in range(len(list_)):
            place = list_[i].find(":", 0, len(list_[i]))
            name = (list_[i])[0:place]
            code = (list_[i])[place+1:len(list_[i])]
            dict_[code] = name
        x = input("Input rgb numbers: ")
        if x in dict_:
            print(dict_[x])
        else:
            print("Color not found")
