# Jakub Radek
# Wydaje mi się, że program w założeniu miał zliczać tylko te trójki liczb których nwd jest równe jeden dla każdej
# możliwej pary tych trzech liczb, dlatego napisałem dwie wersje, funkcja trojki liczy gdy nwd tych trzech liczb jest
# rowne 1 a funkcja trojki_alt liczy gdy nwd jest rowne 1 dla kazdej pary tych liczb
# Sama funkcja działa na zasadzie wybierania trójki możliwych indeksów takich by elementy z nich spełniały warunek zadania
# a następnie sprawdza nwd, tu już metoda inna w zależności od funkcji, a potem zwraca ilość sytuacji gdzie warunki zadania
# były spełnione


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        b, a = a % b, b
    return a


def trojki(T):
    length = len(T)
    counter = 0
    for i in range(length-2):
        for j in range(i+1, i+3):
            for k in range(j+1, j+3):
                if j < length-1 and k < length:
                    n = gcd(T[i],T[j])
                    n = gcd(n,T[k])
                    if n == 1:
                        counter += 1
    return counter


def trojki_alt(T):
    length = len(T)
    counter = 0
    for i in range(length-2):
        for j in range(i+1, i+3):
            for k in range(j+1, j+3):
                if j < length-1 and k < length:
                    n1 = gcd(T[i],T[j])
                    n2 = gcd(T[j],T[k])
                    n3 = gcd(T[i],T[k])
                    if n1 == 1 and n2 == 1 and n3 == 1:
                        counter += 1
    return counter