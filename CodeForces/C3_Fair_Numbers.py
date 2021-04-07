def func(num, tab):
    check = True
    for j in range(len(tab)):
        if tab[j] != 0:
            if num % tab[j] != 0:
                check = False
    return check


def split_tab(num, list_):
    while num > 0:
        list_.append(num % 10)
        num //= 10
    return list_.reverse()


T = int(input())
for i in range(T):
    number = int(input())
    list_ = []
    split_tab(number, list_)
    if func(number, list_):
        print(number)
    else:
        j = number
        while j < 1000000000000000000000000000000:
            list_.clear()
            j += 1
            split_tab(j, list_)
            if func(j, list_):
                print(j)
                j = 1000000000000000000000000000000
