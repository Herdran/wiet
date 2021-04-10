def printAllLIS(A):
    print(A)
    n = len(A)
    g = [1]*n

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and g[j]+1 > g[i]:
                g[i] = g[j]+1
    max_len = max(g)

    array = [0]
    printsolution(A, len(A)-1, g, max_len, array, max_len)
    print(array[0])



def printsolution(A, i, g, length, array, max_len):
    if length == 0:
        for _ in range(max_len):
            print(array[max_len-_], end=" ")
        print()
        array[0] += 1
    for j in range(i, -1, -1):
        if g[j] == length:
            array.append(A[j])
            printsolution(A, j, g, length-1, array, max_len)
            array.pop(-1)


A = [3, 1, 5, 7, 2]
A = [2, 1, 4, 3]
A = [10, 22, 42, 33, 21, 50, 41, 60, 80, 3]
printAllLIS(A)