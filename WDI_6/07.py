"""Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie
określonej masy. Odważniki można umieszczać tylko na jednej szalce"""
def cw_07(weight, index=0, sum_=0):
    if sum_ == weight : return True
    if index == len(arr): return False
    else:
        return cw_07(weight, index + 1, sum_ + arr[index]) or cw_07(weight, index + 1, sum_)


if __name__ == '__main__':
    weight = 16
    arr = [1, 7, 3, 5, 11, 2]
    print(cw_07(weight))
