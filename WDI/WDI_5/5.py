"""Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
[(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze
istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
punktów."""


def distance(a, b):
    if a[0] - b[0] != 0:
        return b[0] - a[0]
    return b[1] - a[1]


def distance_diagonally(a, b):
    return b[0] - a[0]


def if_points_inside(a, b, data, distance):
    if distance == 1:
        return False
    for i in range(a, a + distance):
        for j in range(b, b + distance):
            for k in range(len(data)):
                if data[k][0] == i and data[k][1] == j and not (
                        (i == a and j == b) or (i == a and j == b + distance) or (i == a + distance and j == b) or (
                        i == a + distance and j == b + distance)):
                    return True
    return False


def cw5(data):
    for i in range(len(data)):
        for k in range(len(data)):
            x, y, z = 0, 0, 0
            for j in range(i + 1 + k, len(data)):
                if data[i][0] == data[j][0] and x == 0:
                    x = distance(data[i], data[j])
                if data[i][1] == data[j][1] and y == 0:
                    y = distance(data[i], data[j])
                if data[i][0] - data[i][1] == data[j][0] - data[j][1] and z == 0:
                    z = distance_diagonally(data[i], data[j])
            if x == y == z and x != 0:
                a = if_points_inside(data[i][0], data[i][1], data, abs(x))
                if a == False:
                    return True
    return False


if __name__ == '__main__':
    data = [[1, 1], [1, 3], [3, 1], [3, 3], [1, 2], [2, 1], [2, 2]]
    print(cw5(data))
