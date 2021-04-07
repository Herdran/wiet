if __name__ == '__main__':

    r1 = ["|", " ", "|", " ", "|", " ", "|"]
    r2 = ["|", " ", "|", " ", "|", " ", "|"]
    r3 = ["|", " ", "|", " ", "|", " ", "|"]
    x = "X"
    y = 0


    def board():
        print(7 * "-")
        print(*r1, sep="")
        print(7 * "-")
        print(*r2, sep="")
        print(7 * "-")
        print(*r3, sep="")
        print(7 * "-")


    def typing():
        global x
        global y
        y = int(input("Choose square: "))
        if y == 1 and r1[1] == " ":
            r1[1] = x
        elif y == 2 and r1[3] == " ":
            r1[3] = x
        elif y == 3 and r1[5] == " ":
            r1[5] = x
        elif y == 4 and r2[1] == " ":
            r2[1] = x
        elif y == 5 and r2[3] == " ":
            r2[3] = x
        elif y == 6 and r2[5] == " ":
            r2[5] = x
        elif y == 7 and r3[1] == " ":
            r3[1] = x
        elif y == 8 and r3[3] == " ":
            r3[3] = x
        elif y == 9 and r3[5] == " ":
            r3[5] = x
        else:
            print("This square is already occupied, choose another one")
            if x == "X":
                x = "O"
            else:
                x = "X"
        if x == "X":
            x = "O"
        else:
            x = "X"

    def win():
        global x
        if r1[1] == r1[3] and r1[3] == r1[5] and r1[1] != " ":
            board()
            print("Player", r1[1], "wins")
            x = 0
        elif r2[1] == r2[3] and r2[3] == r2[5] and r2[1] != " ":
            board()
            print("Player", r2[1], "wins")
            x = 0
        elif r3[1] == r3[3] and r3[3] == r3[5] and r3[1] != " ":
            board()
            print("Player", r3[1], "wins")
            x = 0
        elif r1[1] == r2[1] and r2[1] == r3[1] and r1[1] != " ":
            board()
            print("Player", r1[1], "wins")
            x = 0
        elif r1[3] == r2[3] and r2[3] == r3[3] and r1[3] != " ":
            board()
            print("Player", r1[3], "wins")
            x = 0
        elif r1[5] == r2[5] and r2[5] == r3[5] and r1[5] != " ":
            board()
            print("Player", r1[5], "wins")
            x = 0
        elif r1[1] == r2[3] and r2[3] == r3[5] and r1[1] != " ":
            board()
            print("Player", r1[1], "wins")
            x = 0
        elif r1[5] == r2[3] and r2[3] == r3[1] and r3[1] != " ":
            board()
            print("Player", r1[5], "wins")
            x = 0


    while x != 0:
        board()
        typing()
        win()
