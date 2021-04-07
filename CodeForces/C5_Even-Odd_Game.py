T = int(input())
for i in range(T):
    length = int(input())
    list_ = list(map(int, input().split()))
    list_ = sorted(list_, reverse=True)
    sum_a = 0
    sum_b = 0
    for i in range(length):
        if i%2==0:
            if list_[i]%2 == 0:
                sum_a += list_[i]
        else:
            if list_[i]%2 == 1:
                sum_b += list_[i]
    if sum_a > sum_b:
        print("Alice")
    elif sum_a < sum_b:
        print("Bob")
    else:
        print("Tie")