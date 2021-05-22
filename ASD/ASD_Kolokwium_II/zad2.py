# Jakub Radek
# Program ten wywołuje BFS z jednego z wierzchołków, wylicza w ten sposób odległość między nimi. Zmodyfikowany BFS zapisuje
# także rodziców każdego wierzchołka. Wywołuję BFS tyle razy jaka jest odległosć, ale bez brania pod uwagę jednej z krawędzi
# która była na oryginalnej drodze, jeśli choć raz odległość punktów zmieni się, to znaczy że odpowiedź istnieje
# Szacowana złożoność to


from queue import Queue
from zad2testy import runtests



def BFS(graph, index,  nokrawedz=False):
    G = [[0] for _ in range(len(graph))]
    visited = [False] * len(graph)
    Q = Queue()

    visited[index] = True
    Q.put([graph[index], index])
    while Q.qsize() > 0:
        u = Q.get()
        for v in u[0]:
            if nokrawedz and ((u[1] == nokrawedz[0] and v == nokrawedz[1]) or (u[1] == nokrawedz[1] and v == nokrawedz[0])):
                continue
            if not visited[v]:
                visited[v] = True
                G[v] = [G[u[1]][0] + 1, u[1]]
                Q.put([graph[v], v])
    return G


def enlarge(G, s, t):
    graph = BFS(G, s)
    G[0] = [0, 0]
    start_length = abs(graph[s][0] - graph[t][0])
    # print(graph, start_length)
    x = t


    while len (graph[x]) > 1 and x != graph[x][1]:
        no_krawedz = (x, graph[x][1])

        # print(no_krawedz)
        graphDDD = BFS(G, s, no_krawedz)
        curr_length = abs(graphDDD[s][0] - graphDDD[t][0])
        # print(curr_length)
        if curr_length < start_length:
            return no_krawedz
        x = graph[x][1]
    return None


# G = [[1, 2], [0, 2], [0, 1]]
G2 = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]


s = 0
t = 3
print(enlarge(G2, s, t))
# runtests( enlarge )
# runtests(enlarge)