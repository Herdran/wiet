T = int(input())
for i in range(T):
    n = int(input())
    text = input()
    counter = 0
    counting = False
    for j in range(n):
        if text[j] == ')':
            counter += 1
            counting = True
        elif counting:
            counting = False
            counter = 0
    if len(text) - counter < counter:
        print("YES")
    else:
        print("NO")