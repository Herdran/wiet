def zad15(size):
    hetmans_positions = [-1] * size
    T0 = [True] * size
    T1 = [True] * (size * 2 - 1)
    T2 = [True] * (size * 2 - 1)
    end_of_rec = False

    def print_result(T):
        for i in range(len(T)):
            for j in range(len(T)):
                if T[i] == j:
                    print("H", end=" ")
                else:
                    print(end=". ")
            print()
        print()

    def hetman(row, col):
        nonlocal end_of_rec
        if not (T0[row] and T1[row+col] and T2[row-col+size-1]):
            return False

        hetmans_positions[col] = row
        if col != size - 1:
            T0[row] = T1[row + col] = T2[row - col + size - 1] = False
            for i in range(size):
                if end_of_rec:
                    return
                hetman(i, col + 1)
            T0[row] = T1[row + col] = T2[row - col + size - 1] = True
        else:
            print_result(hetmans_positions)
            end_of_rec = True

    for i in range(size):
        hetman(i, 0)


zad15(6)
print("Koniec")

