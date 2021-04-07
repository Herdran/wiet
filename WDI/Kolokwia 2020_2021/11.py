def zad(T):
    def suma(t, r1, c1, r2, c2, sum_of_col, sum_of_row):
        temp_sum = sum_of_col[c1] + sum_of_col[c2] + sum_of_row[r1] + sum_of_row[r2]
        if r1 == r2 and c1 == c2:
            temp_sum -= sum_of_row[r1] + sum_of_col[c1] + 2 * T[r1][c1]
        elif r1 == r2:
            temp_sum -= sum_of_row[r1] + 2 * T[r1][c1] + 2 * T[r2][c2]
        elif c1 == c2:
            temp_sum -= sum_of_col[r1] + 2 * T[r1][c1] + 2 * T[r2][c2]
        else:
            temp_sum -= T[r1][c1] + T[r2][c2]
        return temp_sum

    # print(suma(T, 2, 2, 2, 2, [13, 5, 5], [6, 3, 14]), "aaaaaaa")
    n = len(T)
    sum_of_col = [0 for i in range(n)]
    sum_of_row = [0 for i in range(n)]

    r1, c1 = 0, 0
    r2, c2 = 0, 0

    for i in range(n * n):
        sum_of_col[i % n] += T[i // n][i % n]
        sum_of_row[i // n] += T[i // n][i % n]

    curr_sum = suma(T, r1, c1, r2, c2, sum_of_col, sum_of_row)

    for i in range(n):
        if i != r1:
            if suma(T, i, c1, r2, c2, sum_of_col, sum_of_row) > curr_sum:
                curr_sum = suma(T, i, c1, r2, c2, sum_of_col, sum_of_row)
        if i != c1:
            if suma(T, r1, i, r2, c2, sum_of_col, sum_of_row) > curr_sum:
                curr_sum = suma(T, i, c1, r2, c2, sum_of_col, sum_of_row)
        if i != r2:
            if suma(T, r1, c1, i, c2, sum_of_col, sum_of_row) > curr_sum:
                curr_sum = suma(T, i, c1, r2, c2, sum_of_col, sum_of_row)
        if i != c2:
            if suma(T, r1, c1, r2, i, sum_of_col, sum_of_row) > curr_sum:
                curr_sum = suma(T, i, c1, r2, c2, sum_of_col, sum_of_row)
        print(curr_sum)


# end

T = [[4, 0, 2],
     [3, 0, 0],
     [6, 5, 3]]

wieza1 = (0, 0)
wieza2 = (0, 0)

print(zad(T))

