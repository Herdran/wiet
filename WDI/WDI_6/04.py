# def can_place(x, y, N):
#
#     if (x < N - 1 and y < N and T[x+2][y+1]) or T[x+2][y-1] or T[x+1][y+2] or T[x+1][y-2] or T[x-2][y+1] or T[x-2][y-1] or T[x-1][y+2] or T[x-1][y-2] == 0:
#         return True
#     return False


def cw_04(x, y, cnt, N):
    # for i in T:
    #     print(i)
    # print(x, y, cnt)
    for _ in T:
        if cnt in _:
            for i in range(N):
                if _[i] == cnt:
                    _[i] = 0
    if x < N - 1 and y < N - 2 and T[x+1][y+2] == cnt - 1 and (T[x][y] != 0 or (N <= x or x < 0 or N <= y or y < 0)):
        T[x+1][y+2] = 0
        return False
    else:
        if 0 <= x < N and 0 <= y < N:
            if T[x][y] == 0:
                if cnt == N*N:
                    return True
                T[x][y] = cnt

                return cw_04(x + 2, y + 1, cnt + 1, N) or \
                       cw_04(x + 2, y - 1, cnt + 1, N) or \
                       cw_04(x + 1, y + 2, cnt + 1, N) or \
                       cw_04(x + 1, y - 2, cnt + 1, N) or \
                       cw_04(x - 2, y + 1, cnt + 1, N) or \
                       cw_04(x - 2, y - 1, cnt + 1, N) or \
                       cw_04(x - 1, y + 2, cnt + 1, N) or \
                       cw_04(x - 1, y - 2, cnt + 1, N)
            else:
                return False


if __name__ == '__main__':
    # N = int(input())
    N = 5
    T = [[0 for _ in range(N)] for _ in range(N)]
    target_cnt = N * N
    # vectors = ((-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1))

    print(cw_04(0, 0, 1, N))
