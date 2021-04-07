from math import sqrt, ceil, log

T = [[randint(1, 10) for _ in range(N)] for _ in range(N)]



def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # end if
        # end for
    #end for
    return(arr)
#end def


def prime(n):
    if n == 2 or n == 3:
        return True
    #end if
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    #end if

    a = 5
    while a <= sqrt(n):
        if n % a == 0:
            return False
        a += 2
        if n % a == 0:
            return False
        a += 4
    #end while
    return True
#end def


def zlozona(n):
    if n <= 3 or n == 5:
        return False
    if n%2 == 0 or n%3 == 0:
        return True

    a = 6
    while a <= n//2:
        if n%(a-1) == 0 or n%(a+1) == 0:
            return True
        a += 6
    #end while
    return False
#end def


def sito(N):
    tab = [True for _ in range(N+1)]
    tab[0] = tab[1] = False

    for i in range(2, ceil(sqrt(N) + 1)):
        if tab[i]:
            for a in range(i*i,N+1,i):
                tab[a] = False
            #end for
        #end if
    #end for

    for i in range(N+1):
        if tab[i]: print(i)
    #end for
#end def


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        b, a = a % b, b
        #end while
    return a
#end def


def co_najmniej_2ga_potega(n):
    podstawa = 2
    while podstawa <= sqrt(n):
        potega = podstawa*podstawa
        while potega <= n:
            if potega == n:
                return True
            potega *= podstawa
        #end while
        podstawa += 1
    #end while
    return False
#end def


def if_power_of_at_least_two(x):
    y = 2
    z = 2
    while y < x:
        while y ** z <= x:
            if y ** z == x:
                return True
            z += 1
        #end while
        y += 1
        z = 2
    # end while
    return False
#end def


def zamiana_podstaw(liczba, podstawa):
    if podstawa < 10:
        new_liczba = 0
        i = 0
        while liczba > 0:
            new_liczba += (liczba%podstawa)*(10**i)
            liczba //= podstawa
            i += 1
        #end while
        return new_liczba
    else:
        new_liczba = ""
        while liczba > 0:
            if liczba%podstawa < 10:
                new_liczba = str(liczba%podstawa) + new_liczba
            #end if
            else:
                new_liczba = str(chr(55+(liczba%podstawa))) + new_liczba
            liczba //= podstawa
        #end while
        return new_liczba
#end def

def into_different_zapisy(number, numeral_system):
    list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    list1_ = [0] * (number // numeral_system + 1)
    i = 0
    length = 0
    while number > 0:
        list1_[i] = (list_[number % numeral_system])
        number //= numeral_system
        i += 1
        length += 1
    #end while
    number = [0] * length
    i = 0
    while length > 0:
        number[i] = list1_[length - 1]
        i += 1
        length -= 1
    #end while
    return number
#end def



def zamiana_podstaw_tab(number, podstawa):
    if number == 0:
        return [0]
    #end if

    hex = "0123456789ABCDEF"
    new_number = [0 for _ in range(ceil(log(number + 1, podstawa)))]
    i = len(new_liczba) - 1
    while number > 0:
        new_number[i] = hex[number%podstawa]
        number //= podstawa
        i -= 1
    #end while
    return new_number
#end def


print(zamiana_podstaw_tab(15, 16))
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print(arr)