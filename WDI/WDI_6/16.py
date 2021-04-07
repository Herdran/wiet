"""Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek oraz
sumy kodów ascii liter z których są zbudowane są identyczne, na przykład "ula" → 117, 108, 97
oraz "exe" → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu
z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
znaleziony wyraz."""
def weight(word):
    sum_ = 0
    for i in range(len(word)):
        sum_ += ord(word[i])
    return sum_


def vovels_check(word1, word2):
    w1, w2 = 0, 0
    for i in range(len(word1)):
        if word1[i] in vowel:
            w1 += 1
    for i in range(len(word2)):
        if word2[i] in vowel:
            w2 += 1
    return w1 == w2


def wyraz(s1, s2):
    if weight(s1) >= weight(s2):
        return False
    else:
        for i in range(len(s2)):
            word = s2[:i] + s2[i+1:]
            if weight(word) > weight(s1):
                return wyraz(s1, word)
            if weight(word) == weight(s1) and vovels_check(s1, word):
                return True


vowel = "aeiou"
s1 = "exe"
s2 = "eeeeexe"
print(wyraz(s1, s2))
