"""Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika."""
from random import randint
from time import time

start_time = time()

def cw_18(x, y):
    def checking_numbers(number_1, number_2):
        n1 = number_1 % 10
        while number_2 > 9:
            number_2 //= 10
        n2 = number_2
        if n1 < n2:
            return True
        return False

    def func(x, y):
        if x + y != 14:
            if x < 7 and y < 7 and checking_numbers(arr[x][y], arr[x+1][y+1]):
                func(x+1, y+1)
            if x < 7 and checking_numbers(arr[x][y], arr[x+1][y]):
                func(x+1, y)
            if y < 7 and checking_numbers(arr[x][y], arr[x][y+1]):
                func(x, y+1)
        else:
            print("Moszna")
            print(time() - start_time)
            exit(0)
    func(x, y)
    return False


# arr = [[randint(10, 12) for _ in range(8)] for _ in range(8)]
arr = [[0, 1, 2, 3, 4, 5, 6, 7],
       [1, 2, 3, 4, 5, 6, 7, 81],
       [1, 2, 3, 4, 5, 6, 7, 2],
       [1, 2, 3, 4, 5, 6, 7, 3],
       [1, 2, 3, 4, 5, 6, 7, 4],
       [1, 2, 3, 4, 5, 6, 7, 5],
       [1, 2, 3, 4, 5, 6, 9, 6],
       [1, 2, 3, 4, 5, 6, 9, 7]]

# for _ in arr:
#     print(_)
print(cw_18(0, 0))
