n = int(input("podaj dokladnosc"))
a = 0
e = [0 for i in range(n + 1)]
s = [0 for i in range(n + 1)]
s[0] = 1

while True:
    # if s == 0: break

    # e = e + s
    p = 0
    for i in range(n, -1, -1):
        e[i] = e[i] + s[i] + p
        p = e[i] // 10
        e[i] = e[i] % 10

    a += 1
    # s = s / a
    r = 0
    kon = True
    for i in range(0, n + 1):
        r = r * 10 + s[i]
        s[i] = r // a
        if s[i] > 0: kon = False
        r = r % a

    if kon: break

# print("e= ", e)
print(e[0], end=".")
for i in range(1, n + 1):
    print(e[i], end="")
