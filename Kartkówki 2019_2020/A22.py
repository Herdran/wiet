"""2. Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
 A: zwiększa liczbę o 3;
 B: podwaja liczbę;
 C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.
Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić liczbę możliwych ciągów operacji
przekształcających liczbę X w Y (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
używanie kolejno dwóch tych samych operacji.
Na przykład:
Dla X=11, Y=31, N=4 funkcja powinna zwrócić 3 bo są 3 możliwe ciągi operacji: ABA, ACBC, CABA
Dla X=11, Y=32, N=4 funkcja powinna zwrócić 0."""


def A(n): return n+3


def B(n): return n*2


def C(n):
    x = n
    j = 0
    while x > 0:
        if (x % 10) % 2 == 0:
            n += 1 * 10**j
        j += 1
        x //= 10
    return n


def func(X, Y, N, path='', length=0, test=0):
    if X == Y:
        print(path)
        flag[0] = True
    if length < N:
        if test != 1: func(A(X), Y, N, path+'A', length+1, 1)
        if test != 2: func(B(X), Y, N, path+'B', length+1, 2)
        if test != 3: func(C(X), Y, N, path+'C', length+1, 3)


flag = [False]
X = 11
Y = 31
N = 4
func(X, Y, N)
if not flag[0]:
    print(0)