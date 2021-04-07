def board():
    for k in range(7):
        if k % 2 == 0:
            print(16 * "-")
        elif k == 1:
            print("| ", area[1], " | ", area[2], " | ", area[3], " |")
        elif k == 3:
            print("| ", area[4], " | ", area[5], " | ", area[6], " |")
        elif k == 5:
            print("| ", area[7], " | ", area[8], " | ", area[9], " |")


def sign_choice():
    player1 = input("Player1 marker - pick X or O: ")
    while True:
        if player1 == "X":
            player2 = "O"
            return player1, player2
        elif player1 == "O":
            player2 = "X"
            return player1, player2
        else:
            player1 = input("Invalid symbol. Player1 marker - pick X or O: ")


def area_choice(w):
    if w == 1:
        print("Player1 turn.")
        sign = player_first
    else:
        print("Player2 turn.")
        sign = player_second
    choice = int(input("Select an empty area: "))
    if choice not in (i for i in range(10)):
        print("Number out of range.")
        return w == 1 if sign == player_first else 1
    if area[choice] == "":
        area[choice] = sign
        return w == 2 if sign == player_first else 1
    else:
        print("This area in unavailable.")
        return w == 1 if sign == player_first else 2


def victory():
    if area[1] == area[2] and area[2] == area[3] and area[1] != " ":
        name = "player1" if area[1] == "X" else "player2"
        print(name, " has won!")
    elif (area[4] == area[5] == area[6]) == ("X" or "Y"):
        name = "player1" if area[4] == "X" else "player2"
        print(name, " has won!")
    elif (area[7] == area[8] == area[9]) == ("X" or "Y"):
        name = "player1" if area[7] == "X" else "player2"
        print(name, " has won!")
    elif (area[1] == area[4] == area[7]) == ("X" or "Y"):
        name = "player1" if area[1] == "X" else "player2"
        print(name, " has won!")
    elif (area[2] == area[5] == area[8]) == ("X" or "Y"):
        name = "player1" if area[2] == "X" else "player2"
        print(name, " has won!")
    elif (area[3] == area[6] == area[9]) == ("X" or "Y"):
        name = "player1" if area[3] == "X" else "player2"
        print(name, " has won!")
    elif (area[1] == area[5] == area[9]) == ("X" or "Y"):
        name = "player1" if area[1] == "X" else "player2"
        print(name, " has won!")
    elif (area[3] == area[5] == area[7]) == ("X" or "Y"):
        name = "player1" if area[3] == "X" else "player2"
        print(name, " has won!")


def draw():
    if area[1] and area[2] and area[3] and area[4] and area[5] and area[6] and area[7] and area[8] and area[9]:
        print("This round finished with a draw.")


if __name__ == "__main__":
    player_first, player_second = sign_choice()
    area = ["" for i in range(10)]
    area[0] = "F"
    board()
    x = 1
    while not (victory() or draw()):
        y = area_choice(x)
        board()
        x = area_choice(y)
        board()
