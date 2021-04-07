T = int(input())
for i in range(T):
    w, h, n = map(int, input().split())
    if n == 1:
        print("YES")
    else:
        w_2 = 0
        h_2 = 0
        i = 0
        while w > 0 and w % 2 == 0:
            w //= 2
            w_2 += 1 * 2**i
            i += 1
        i = 0
        while h > 0 and h % 2 == 0:
            h //= 2
            h_2 += 1 * 2**i
            i += 1
        if (w_2+1)*(h_2+1) >= n:
            print("YES")
        else:
            print("NO")