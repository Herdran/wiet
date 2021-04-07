def recursion(index, n):
    if index == n and stop_[0] != True:
        sum_ = 0
        for k in range(n):
            sum_ += abs(list1_[k]-list2_[k])
        sum_ *= 2
        if sum_ <= sum(list1_) and stop_[0] != True:
            print(*list2_)
            stop_[0] = True
    else:
        j = 1
        while j < 10**9:
            if j >= 2 * sum(list1_):
                j = 10 ** 9
            elif index == 0 or (list2_[index-1] % j == 0 or j % list2_[index-1] == 0) and stop_[0] != True:
                list2_[index] = j
                recursion(index+1, n)
                if stop_[0] == True:
                    j = 10**9
            j += 1

T = int(input())
for i in range(T):
    stop_ = [False]
    n = int(input())
    numbers = input()
    list1_ = list(map(int, numbers.split()))
    sum1_ = sum(list1_)
    j = 1
    while j < n:
        if list1_[j-1] % list1_[j] == 0 or list1_[j] % list1_[j-1] == 0:
            j += 1
        else:
            j = n+1
    if j == n:
        print(*list1_)
    else:
        list2_ = [0] * n
        recursion(0, n)