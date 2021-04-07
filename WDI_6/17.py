"""Zadanie 17. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą
wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb."""
def prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    a = 5
    while a <= n**(1/2):
        if n % a == 0:
            return False
        a += 2
        if n % a == 0:
            return False
        a += 4
    return True


def cw_17(s1, s2, number="", x=0, y=0):
    if x >= len(s1) and y < len(s2):
        cw_17(s1, s2, number+s2[y], x, y+1)
    elif x < len(s1) and y >= len(s2):
        cw_17(s1, s2, number + s1[x], x + 1, y)
    else:
        if x + y == len(s1) + len(s2):
            if prime(int(number)):
                primes.add(int(number))
        else:
            cw_17(s1, s2, number+s1[x], x+1, y) or cw_17(s1, s2, number+s2[y], x, y+1)


s1 = "121"
s2 = "111"
primes = set()
cw_17(s1, s2)
print(primes, len(primes))
