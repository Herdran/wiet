T = int(input())
for i in range(T):
    sum_ = int(input())
    list_ = list(map(int, input().split()))
    if sum(list_) % 2 != 0:
        print("NO")
    else:
        c1 = list_.count(1)
        c2 = list_.count(2)
        if c1 % 2 != 0:
            print("NO")
        if c2 % 2 != 0:
            if c1 >= 2:
                print("YES")
            else:
                print("NO")
        else:
            print("YES")
