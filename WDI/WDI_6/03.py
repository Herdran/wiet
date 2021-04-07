"""Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi
koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia."""


# def cw_03(list_, row, column, list_of_results, sum_):
#     if row != 7:
#         cw_03(list_, row + 1, column, list_of_results, sum_ + list_[row + 1][column])
#         if column < 7:
#             cw_03(list_, row + 1, column + 1, list_of_results, sum_ + list_[row + 1][column + 1])
#         if column > 0:
#             cw_03(list_, row + 1, column - 1, list_of_results, sum_ + list_[row + 1][column - 1])
#     if row == 7:
#         list_of_results.append(sum_)
#     return list_of_results


def cw_03(list_, row, column, sum_):
    if row == 7:
        return sum_
    else:
        if 0 <= column <= 7:
            r2, r3 = 10**10, 10**10
            r1 = cw_03(list_, row + 1, column, sum_ + list_[row + 1][column])
            if column < 7:
                r2 = cw_03(list_, row + 1, column + 1, sum_ + list_[row + 1][column + 1])
            if column > 0:
                r3 = cw_03(list_, row + 1, column - 1, sum_ + list_[row + 1][column - 1])
            return min(r1, r2, r3)
        else:
            return 10**10

    # return list_of_results


if __name__ == '__main__':
    list_ = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
    k = 0
    print(cw_03(list_, 0, k, list_[0][k]))