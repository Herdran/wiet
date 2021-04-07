def chess_king(T, k, i=0, result=0):
    result += T[i][k]
    summary = -1
    if i == 7:
        return result
    else:
        for j in range(k-1, k+2):
            if j >= 0 and j < 8:
                if summary == -1:
                    summary = chess_king(T, j, i+1, result)
                else:
                    summary = min(chess_king(T, j, i+1, result), summary)
    return summary

k = 0
T = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
print(chess_king(T, k))