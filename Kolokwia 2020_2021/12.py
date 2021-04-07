# Jakub Radek Program dzieli tablice na ileś kawałków z który każdy kawałek jest liczbą pierwszą a potem sprawdza
# wszystkie możliwości

def is_prime(n):
    if n == 2:
        return True
    if n == 0 or n == 1 or n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
#end def


def is_prime_tab(n):
    x = 0
    for i in n:
        x *= 10
        x += i
    return is_prime(x)
#end def


def sub_divide(left, tab, mylen):
    if left == 1:
        return is_prime_tab(tab)
    for i in range(1, mylen + 1):
        if is_prime_tab(tab[0:i]) and sub_divide(left - 1, tab[i:], mylen - (i - 1)):
            return True
    return False
#end def


def divide(N):
    if N == 0:
        return False
    ln = 0
    ncpy = N
    while ncpy > 0:
        ncpy = ncpy // 10
        ln += 1
    tab = [0] * ln
    ncpy = N
    for i in range(ln):
        tab[ln - i - 1] = ncpy % 10
        ncpy = ncpy // 10

    for i in range(ln+1):
        if is_prime(i) and sub_divide(i, tab, ln):
            return True
    return False
#end def