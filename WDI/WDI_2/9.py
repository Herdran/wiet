if __name__ == '__main__':
    k = 11
    n = 10
    a = 1
    b = k
    p = 0
    x = (k-1)/n

    for i in range(0, n):
        y = 1/(a+((b-1)/(2*n))+i*x)
        p += x*y
    print(p)
