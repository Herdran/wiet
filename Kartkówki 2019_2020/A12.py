def jedynki_row(list_):
    for i in range(len(list_)):
        x = list_[i]
        y = 0
        while x > 0:
            if x % 10 == 1:
                y += 1
            x //= 10
        if y % 2 == 0:
            return False
    return True


def jedynki_column(list_, a, deleted_row):
    for i in range(len(list_)):
        if i != deleted_row:
            x = list_[i][a]
            y = 0
            while x > 0:
                if x % 10 == 1:
                    y += 1
                x //= 10
            if y % 2 == 0:
                return False
    return True


def check_rows(t):
    row = False
    for i in range(len(t)):
        row = jedynki_row(t[i])
        if row == False:
            rows_to_delete += 1
            column = check_colums(t, i)
            print(column, i)
    if row == True:
        for i in range(len(t)):
            column = check_colums(t, i)
        if column == row:
            return False


def check_colums(t, deleted_row):
    print("nani")
    for i in range(len(t)):
        column_1 = jedynki_column(t, i, deleted_row)
        if column_1 == False:
            for j in range(i + 1, len(t)):
                column_2 = jedynki_column(t, j, deleted_row)
        if column_1 == column_2 == False:
            return True
    return True

        # if row == False:
        #     column = check_colums(t, i)
        # if column == row:
        #     return False





t = [[10, 21, 31], [10, 20, 30], [10, 20, 30]]

print(check_rows(t))
