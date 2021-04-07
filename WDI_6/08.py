"""Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach."""


def cw_08(weight, index=0, sum_=0):
    if sum_ == weight: return True
    if index == len(arr): return False
    else:
        return cw_08(weight, index + 1, sum_ + arr[index]) or cw_08(weight, index + 1, sum_) or cw_08(weight, index + 1, sum_ - arr[index])


if __name__ == '__main__':
    weight = 16
    arr = [1, 7, 3, 5, 11, 2]
    print(cw_08(weight))
