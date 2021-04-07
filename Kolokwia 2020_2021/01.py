# Jakub Radek
def multi(T):
    n = len(T)
    final_length = 0
    for i in range(n):
        length = len(T[i])
        for j in range(length):
            current_length = 0
            for k in range(length):
                if T[i][j] == T[i][k]:
                    current_length += 1
                    print(T[i][j], T[i][k])
                # end if
            #end for
            if final_length < current_length:
                final_length = current_length
            #end if
        #end for
    #end for
    return final_length
#end def

T = ["ABC", "ABC", "ABC"]
print(multi(T))