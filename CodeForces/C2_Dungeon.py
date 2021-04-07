T = int(input())
for i in range(T):
    number = input()
    list_ = list(map(int, number.split()))
    sum_ = sum(list_)
    if sum_ >= 9 and sum_ % 9 == 0:
        length = sum_ // 9
        temp = True
        if list_[0] >= length and list_[1] >= length and list_[2] >= length:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
