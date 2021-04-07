"""Zadanie 6. Liczby zespolone są reprezentowane przez krotkę (re, im). Gdzie: re - część rzeczywista liczby,
im - część urojona liczby. Proszę napisać podstawowe operacje na liczbach zespolonych, m.in. dodawanie,
odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie."""

import math


def create():
    l, m = (input("Input: ").split())
    return int(l), int(m)


def output(n):
    print(f"({n[0]}, {n[1]}i)")


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)


def addition(a, b):
    return a[0]+b[0], a[1]+b[1]


def substraction(a, b):
    return a[0]-b[0], a[1]-b[1]


def multiplication(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def division(a, b):
    return (a[0]*b[0] + a[1]*b[1]) / ((b[0]*b[0]) + (b[1] * b[1])), (a[1]*b[0] - a[0]*b[1]) / ((b[0]*b[0]) + (b[1] * b[1]))


def exponentiation(a, n):
    absolute_value = (a[0]*a[0]-a[1]*a[1])**(1/2)
    arg = math.cos(a[0]/absolute_value)**(-1)
    print(absolute_value, arg, a, n)
    return (absolute_value**n/2)*math.cos(math.pi * n * arg), (absolute_value**n/2)*math.sin(math.pi * n * arg)

if __name__ == '__main__':
    # a = create()
    # b = create()
    # output(a)
    a = (2, 0)
    # print(addition(a, b))
    # print(substraction(a, b))
    # print(multiplication(a, b))
    # print(division(a, b))
    # print(exponentiation(a, 19))
    # print(a)

    # absolute_value = (a[0]*a[0]+a[1]*a[1])**(1/2)
    # arg = math.cos(a[0]/absolute_value)**(-1)
    # print(absolute_value, arg)
    arg = math.pi/6
    print(math.cos(arg))
    print(math.sin(arg))