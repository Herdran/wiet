"""Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję, która
odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać położenie hetmanów."""


def check_checkmate(data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i][0] == data[j][0]:
                return False
            if data[i][1] == data[j][1]:
                return False
            x = abs(data[i][0] - data[j][0])
            y = abs(data[i][1] - data[j][1])
            if x // y == 1 or x//y == -1:
                return False
    return True

if __name__ == '__main__':
    n = 4
    board = [[0] * n] * n
    # print(board)
    data = [[1, 1], [2, 3], [3, 3], [2, 0]]
    # print(data)
    print(check_checkmate(data))

