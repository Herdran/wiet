from random import seed, randint
import time


def knapsack(W, P, MaxW):
    n = len(W)
    F = [[0] * (MaxW + 1) for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
    return F[n - 1][MaxW], F


def get_solution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]: return [0]
        return []
    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]
    return get_solution(F, W, P, i - 1, w)


# P = [10, 8, 4, 5, 3, 7]
# W = [4, 5, 12, 9, 1, 13]
# MaxW = 24

# P = [2, 1, 4, 3]
# W = [2, 1, 1, 2]
# MaxW = 3
seed(41)

n = 100
P = [randint(0, 10000) for i in range(n)]
W = [randint(0, 10000) for i in range(n)]
MaxW = 14500
start_time = time.time()
res, F = knapsack(W, P, MaxW)
solution = 0
# solution = get_solution(F, W, P, len(P) - 1, MaxW)
print(res, solution)
print("--- %s seconds ---" % (time.time() - start_time))