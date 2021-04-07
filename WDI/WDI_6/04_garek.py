from time import time
start_time = time()


def if_move_possible(arr, i, x, y):
    vectors = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    x += vectors[i][0]
    y += vectors[i][1]
    if x >= 0 and y >= 0 and x < len(arr) and y < len(arr) and arr[x][y] == 0:
        return x, y
    return False


def horse_jump(arr, x=0, y=0, counter=1):
    arr[x][y] = counter
    if counter == len(arr) ** 2:
        # for _ in arr:
        #     print(_)
        print_result(arr)
        exit(0)
    else:
        for i in range(8):
            r = if_move_possible(arr, i, x, y)
            if r:
                horse_jump(arr, r[0], r[1], counter + 1)
        arr[x][y] = 0


def print_result(T):
    for i in range(len(T)):
        for j in range(len(T)):
            print(T[i][j], end="\t")
        print()
    print(time() - start_time)

N = 6
arr = [[0 for _ in range(N)] for _ in range(N)]
horse_jump(arr)
