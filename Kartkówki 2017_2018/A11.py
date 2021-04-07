list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
number1_ = int(input("Number 1: "))
number2_ = int(input("Number 2: "))
z = 2
while z <= 16:
    x = number1_
    y = number2_
    list1_ = []
    list2_ = []
    while x > 0 or y > 0:
        list1_.append(x % z)
        x //= z
        list2_.append(y % z)
        y //= z
    list1_.reverse()
    list2_.reverse()
    a = True
    for i in range(len(list1_)):
        if list1_[i] in list2_:
            a = False
            break
    if a == True:
        print("Najmniejsza podstawa która spełnia warunki zadania to:", z)
        print(list1_, list2_)
        z = 17
    z += 1
