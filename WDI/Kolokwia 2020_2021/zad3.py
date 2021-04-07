# Jakub Radek Program ten sprawdza wszystkie możliwosci i jesli nowa mozliwosc daje wieksza suma to ja
# zapisuje, razem z pozycjami a potem to zwraca
def chess(T):
    n = len(T)
    score = 0
    pos = None
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    ans = 0
                    if i != k:
                        for a in range(n):
                            if a != j:
                                ans += T[i][a]
                            if a != l:
                                ans += T[k][a]
                    else:
                        for a in range(n):
                            if a != j and a != l:
                                ans += T[i][a]
                    if j != l:
                        for a in range(n):
                            if a != i:
                                ans += T[a][j]
                            if a != k:
                                ans += T[a][l]
                    else:
                        for a in range(n):
                            if a != i and a != k:
                                ans += T[a][j]
                    if i != k and j != l:
                        ans -= T[i][l]
                        ans -= T[k][j]
                    if ans > score:
                        score = ans
                        pos = i, j, k, l
    return pos
# end def
