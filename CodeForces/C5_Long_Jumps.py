T = int(input())
for i in range(T):
    length = int(input())
    list_ = list(map(int, input().split()))
    list3_ = [0]*length
    pos = [0]*length
    max_n = max(list_)
    for i in range(length):
        j = i
        sum_ = 0
        while j < length:
            sum_ += list_[j]
            if sum_ >= max_n:
                list3_[i] = 1
                j = length
            if j < length:
                j += list_[j]

    max_sum = 0
    for i in range(length):
        if list3_[i] == 0:
            pass
        else:
            j = i
            sum_ = 0
            while j < length:
                sum_ += list_[j]
                j += list_[j]
            if sum_ >= max_n and sum_ > max_sum:
                max_sum = sum_
    print(max_sum)
