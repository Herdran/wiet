import time
from random import seed, randint


# P = [2, 1, 4, 3]
# W = [2, 1, 1, 2]
# MaxW = 3

# P = [10, 8, 4, 5, 3, 7]
# W = [4, 5, 12, 9, 1, 13]
# MaxW = 24

seed(41)
n = 100
P = [randint(0, 10000) for i in range(n)]
W = [randint(0, 10000) for i in range(n)]
MaxW = 14500
start_time = time.time()
# n = len(P)
M = [0]*(MaxW+1)
for i in range(n):
    for k in range(MaxW, W[i]-1, -1):
        M[k] = max(M[k], M[k-W[i]]+P[i])
print(max(M))
print("--- %s seconds ---" % (time.time() - start_time))
