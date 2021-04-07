T = int(input())
list_ = []
list2_ = []
for i in range(T):
    list_.append(int(input()))
for i in range(T):
    if list_[i] < 10:
        length = 1
        sum_ = list_[i]
        j = 1
    else:
        length = 2
        sum_ = list_[i]
        j = 10
    if length == 1:
        while j < 10:
            if sum_ == j:
                print(j)
                j = 11
            j += 1
        if j != 12:
            print(-1)
    else:
        while j < 123456790:
            test = True
            test2 = True
            x = j
            number = 0
            length = 0
            while x > 0 and test2:
                if number == x % 10 and x % 10 != 0:
                    test2 = False
                number += x % 10
                length += 1
                list2_.append(x % 10)
                x //= 10
            if test2:
                for a in range(len(list2_)):
                    for b in range(a+1, len(list2_)):
                        if list2_[a] == list2_[b]:
                            test = False
                if test:
                    if sum_ == number:
                        print(j)
                        j = 123456790
            print(j)
            j += 1
            list2_.clear()
        if test == False:
            print(-1)