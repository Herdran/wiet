"""Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe."""
def prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    a = 5
    while a <= (n)**(1/2):
        if n % a == 0:
            return False
        a += 2
        if n % a == 0:
            return False
        a += 4
    return True


def cw_05(index=0):
    if index == len(arr):
        return True
    else:
        sum_ = 0
        for i in range(index, min(len(arr), index+30)):
            sum_ = 2 * sum_ + arr[i]
            # if prime(sum_):
            #     print(sum_)
            if prime(sum_) and cw_05(i + 1):
                return True
        return False


if __name__ == '__main__':
    arr = [1, 1, 1, 0, 1, 1]
    print(cw_05())
