"""Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)
"""
def det_2_2(tab, x, rows):
    return (tab[rows[0]][x] * tab[rows[1]][x+1]) - (tab[rows[0]][x+1] * tab[rows[1]][x])

# def cw_10():
#
#


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
N = 4

# wycinanie 1 kolumny i wiersza np
x = 0
y = 0
N -= 1

new_arr = [[0 for _ in range(N)] for _ in range(N)]
x_ = 0
y_ = 0
for i in range(N):
    for j in range(N):
        if x_ != x:
            if y_ != y:
                new_arr[i][j] = arr[x_][y_]
            else:
                y_ += 1
                new_arr[i][j] = arr[x_][y_]
            y_ += 1
        else:
            x_ += 1
            if y_ != y:
                new_arr[i][j] = arr[x_][y_]
            else:
                y_ += 1
                new_arr[i][j] = arr[x_][y_]
            y_ += 1
    y_ = 0
    x_ += 1

print(new_arr)
