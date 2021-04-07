from time import time

start_time = time()


def zad15():
    hetmans_positions = [-1] * 8
    row_tab = [True] * 8
    diagonals_1 = [True] * 15
    diagonals_2 = [True] * 15

    def printing(t):
        for i in t:
            print(i + 1, end=" ")
        print()

    def hetman(row, column):
        if not (row_tab[row] and diagonals_1[row + column] and diagonals_2[row - column + 7]):
            return None
        hetmans_positions[column] = row
        if column != 7:
            row_tab[row] = False
            diagonals_1[row + column] = False
            diagonals_2[row - column + 7] = False
            for j in range(8):
                hetman(j, column + 1)
            row_tab[row] = True
            diagonals_1[row + column] = True
            diagonals_2[row - column + 7] = True
        else:
            printing(hetmans_positions)
        return

    for i in range(0, 8):
        hetman(i, 0)


zad15()
print(time() - start_time)
