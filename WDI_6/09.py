"""Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki."""


def cw_09(weight, path, i=0, sum_=0):
    if abs(sum_) == weight: return path
    if i == len(arr):
        return False
    else:
        return cw_09(weight, f"{path}A:{arr[i]} ", i + 1, sum_ + arr[i], ) or \
               cw_09(weight, f"{path}B:{arr[i]} ", i + 1, sum_, ) or cw_09(weight, path, i + 1, sum_ - arr[i])


if __name__ == '__main__':
    weight = 16
    arr = [1, 7, 3, 5, 11, 2]
    print(cw_09(weight, ""))
