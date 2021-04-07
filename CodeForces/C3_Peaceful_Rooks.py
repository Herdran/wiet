def diagonal(pos):
    if pos[0] == pos[1]:
        return True
    return False


def move(pos, num_of_rook):
    for i in range(size):
        if i != pos[1] and not_in_check(pos[0], i, pos[1], 'x'):
            list_of_pos[num_of_rook] = tuple([pos[0], i])
            return True
    for i in range(size):
        if i != pos[0] and not_in_check(i, pos[1], pos[0], 'y'):
            list_of_pos[num_of_rook] = tuple(i, pos[1])
            return True
    return False


def move_into_diag(pos, num_of_rook):
    if not_in_check(pos[0], pos[0], pos[1], 'x'):
        list_of_pos[num_of_rook] = tuple([pos[0], pos[0]])
        return True
    elif not_in_check(pos[1], pos[1], pos[0], 'y'):
        list_of_pos[num_of_rook] = tuple([pos[1], pos[1]])
        return True
    return False


def not_in_check(x, y, old, axis):
    if axis == 'x':
        if list_of_row[y-1] == False:
            list_of_row[y-1] = True
            list_of_row[old-1] = False
            return True
    else:
        if list_of_col[x-1] == False:
            list_of_col[x-1] = True
            list_of_col[old-1] = False
            return True
    return False


T = int(input())
for i in range(T):
    size, amount = map(int, input().split())
    list_of_pos = []
    list_of_col = [False] * size
    list_of_row = [False] * size
    list_of_cor_pos = [1] * amount
    for j in range(amount):
        list_of_pos.append(tuple(map(int, input().split())))
    for j in range(size):
        for k in range(amount):
            if j+1 == list_of_pos[k][0]:
                list_of_col[j] = True
            if j+1 == list_of_pos[k][1]:
                list_of_row[j] = True

    for j in range(amount):
        if diagonal(list_of_pos[j]):
            list_of_cor_pos[j] = 0

    for j in range(amount):
        if diagonal(list_of_pos[j]):
            list_of_cor_pos[j] = 0

    moves = 0
    while sum(list_of_cor_pos) != 0:
        j = 0
        starting_moves = moves
        while j < amount:
            if list_of_cor_pos[j] == 1:
                if move_into_diag(list_of_pos[j], j):
                    list_of_cor_pos[j] = 0
                    moves += 1
            j += 1
        if moves == starting_moves and sum(list_of_cor_pos) != 0:
            k = 0
            while k < amount:
                if list_of_cor_pos[k] == 1:
                    if move(list_of_pos[k], k):
                        moves += 1
                        k = amount
                k += 1

    print(moves)
