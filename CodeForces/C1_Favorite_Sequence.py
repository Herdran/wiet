T = int(input())
list_ = []
list2_ = []
for i in range(T):
    n = int(input())
    list2_.append(int(n))
    x = input()
    j = 0
    while j < len(x):
        if x[j] != 0:
            if j < len(x) - 1 and x[j + 1] == 0:
                list_.append(int(x[j]))
            else:
                z = 0
                while j < len(x) and x[j] != ' ':
                    z *= 10
                    z += int(x[j])
                    j += 1
                list_.append(z)
        j += 1
shift = 0
for i in range(T):
    combination = ""
    x = True
    y = 0
    n = shift
    for j in range(list2_[i]):
        combination += f'{list_[n]} '
        if x:
            n += list2_[i] - 1
            n -= y
            x = False
        else:
            n -= list2_[i]
            n += y + 1
            x = True
        y += 1
    print(combination)
    shift += list2_[i]
