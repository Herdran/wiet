from copy import deepcopy


def euler(G):
    # standardowy algorytm DFS z wykładu, lekko zmodyfikowany
    def DFSVisit(graph, u):
        # żeby uniknąć konieczności przechodzenia bo tablicy krawędzi dla danego wierzchołka potencjalnie n razy dla grafu
        # pełnego, zapisuję ostatni niesprawdzony indeks do osobnej tablicy i od niego zaczynam
        v = indexes[u]
        visited[u] = True
        while v < length:
            if graph[v][u] == 1:
                graph[v][u] = 0
                graph[u][v] = 0
                indexes[u] = v+1
                DFSVisit(graph, v)
                cycle.append(v)
            v += 1

    length = len(G)

    # sprawdzam czy każdy wierzchołek ma parzystą liczbę krawędzi, jeśli nie, zwracam None
    for u in range(length):
        counter = 0
        for v in range(length):
            if G[u][v] == 1:
                counter += 1
        if counter > 0 and counter % 2 != 0:
            return None

    # kopiuję graf metodą list comprehension
    graph = [[G[_][__] for _ in range(length)] for __ in range(length)]
    # graph = deepcopy(G)
    visited = [False]*length
    indexes = [0 for _ in range(length)]
    cycle = []

    # wywołuję funkcję DFSVisit
    DFSVisit(graph, 0)
    # jeśli graf jest spójny to każdy wierzchołek będzie odwiedzony, to nie będzie żadnej wartości False w tablicy visited
    if False in visited:
        return None
    # wiem teraz że cykl istnieje, dopisuję więc pierwszy element tablicy cycle na koniec, aby cykl zaczynał się i kończył
    # na tym samym wierzchołku
    cycle.append(cycle[0])
    return cycle


# G = [[0, 1, 1, 0, 0, 0],
#      [1, 0, 1, 1, 0, 1],
#      [1, 1, 0, 0, 1, 1],
#      [0, 1, 0, 0, 0, 1],
#      [0, 0, 1, 0, 0, 1],
#      [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")