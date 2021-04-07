def subset(T, k, j, _sum, i):
    if _sum == 0 and k == j == target: return True
    if k > target or j > target or i >= N: return False
    return subset(T, k+1, j, _sum+T[i], i+1) or \
           subset(T, k, j+1, _sum-T[i], i+1) or \
           subset(T, k, j, _sum, i+1)


T = [1, 5, 0, 6]
target = k = int(input())
N = len(T)
print(subset(T, 0, 0, 0, 0))