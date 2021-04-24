from queue import PriorityQueue
import time


def assigning(array, index, code):
    array[index][3] += code
    if array[index][1] == "node":
        assigning(array, array[index][4], code+'0')
        assigning(array, array[index][5], code+'1')


def huffman(S, F):
    length = len(S)
    starting_array = PriorityQueue()
    for i in range(length):
        starting_array.put([F[i], S[i], i, ""])
    final_array = []
    index = 0
    while not starting_array.empty():
        final_array.append(starting_array.get())
        final_array.append(starting_array.get())

        if starting_array.empty():
            break
        starting_array.put([final_array[index][0]+final_array[index+1][0], "node", 0, "", index+1, index+0])
        index += 2

    assigning(final_array, len(final_array)-1, '0')
    assigning(final_array, len(final_array)-2, '1')

    sorter = lambda x: (x[2])
    final_array = sorted(final_array, key=sorter)
    counter = 0
    for i in range(len(final_array)):
        if final_array[i][1] != 'node':
            print(final_array[i][1], ":", final_array[i][3])
            counter += len(final_array[i][3])*final_array[i][0]
    print("dlugosc napisu:", counter)



# S = ["a", "b", "c", "d", "e", "f"]
# F = [10, 11, 7, 13, 1, 20]

S = ['a', 'b', 'c', 'd', 'e', 'f']
F = [5, 9, 12, 13, 16, 45]

S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']
F = [27, 32, 123, 15, 4, 32, 23, 13, 44, 32, 12, 5, 3, 145, 54, 34, 98, 102, 76, 243, 45, 65, 78]

# S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']
# F = [27, 32, 123, 15, 4, 31, 23, 13, 44, 38, 12, 5, 3, 145, 54, 34, 98, 102, 76, 243, 45, 65, 78]

start_time = time.time()
huffman(S, F)
print("--- %s seconds ---" % (time.time() - start_time))