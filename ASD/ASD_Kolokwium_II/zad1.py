# Jakub Radek
# Algorytm opiera się na tablicy dp zawierającej dp[maskymalne użyte pole][dokładna użyta kwota] = maskymalna ilość studentów, numer budynku najbardziej w prawo
# tworzymy nową tablicę array zawierającą oryginalną listę budynków (wraz z ich indeksami z wejściowej tabeli T),
# którą następnie sortujemy rosnąco względem lewego końca budynku następnie przechodzimy po dp a na końcu dokonujemy backtrackingu
# żeby uzyskać rozwiązanie. Szacowana złożoność tego algorytmu to O(n log n + (max b)*p)

from zad1testy import runtests


def select_buildings(T, p):
    building_count = len(T)
    current_building = 0

    array = [None] * building_count

    for i in range(building_count):
        h, a, b, w = T[i]
        array[i] = h * (b - a), a, b, w, i

    array.sort(key=lambda x: x[2])

    total_length = array[-1][2] + 1

    dp = [None for _ in range(total_length)]

    for i in range(total_length):
        if i == 0:
            dp[i] = [(0, -1)] * (p + 1)
        else:
            dp[i] = dp[i - 1][:]

        while current_building < building_count and array[current_building][2] == i:
            size, a, b, w, building_number_int_T = array[current_building]
            current_building += 1

            for val in range(w, p + 1):
                old_size = 0
                if a > 0:
                    old_size = dp[a - 1][val - w][0]

                if old_size + size > dp[i][val][0]:
                    dp[i][val] = old_size + size, building_number_int_T

    max_found, last, price = 0, -1, 0
    for x in range(p + 1):
        if dp[-1][x][0] > max_found:
            max_found, last, price = dp[-1][x][0], dp[-1][x][1], x

    answer = []
    while price != 0:
        answer.append(last)
        price = price - T[last][3]
        last = dp[T[last][1] - 1][price][1]

    answer.sort()

    return answer


runtests(select_buildings)
