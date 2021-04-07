T = int(input())
list_ = []
list2_ = []
for i in range(T):
    n = int(input())
    list2_.append(n)
    x = input()
    for j in range(0, len(x), 2):
        list_.append(int(x[j]))
shift = 0
for i in range(T):
    check = False
    for j in range(list2_[i]):
        x = list_[j + shift]
        for k in range(list2_[i]):
            if list_[k + shift] != x:
                y = list_[k + shift]
                for l in range(list2_[i]):
                    if list_[l + shift] != x and list_[l + shift] != y:
                        z = list_[l + shift]
                        if x < y < z and list_[x + shift - 1] < list_[y + shift - 1] and list_[y + shift - 1] > list_[z + shift - 1]:
                            check = True
                            triple = f'{x} {y} {z}'
    if check:
        print("YES")
        print(triple)
    else:
        print("NO")
    shift += list2_[i]
