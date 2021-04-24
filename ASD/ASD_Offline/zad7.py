from queue import PriorityQueue
import time
import timeit


# funkcja przypisująca kody
def assigning(array, index, code):
    # przypisujemy aktualny kod
    array[index][3] = code
    if array[index][1] == "node":
        # idziemy w prawo i dodajemy 1 do kodu
        assigning(array, array[index][4], code+'0')
        # idziemy w lewo i dodajemy 1 do kodu
        assigning(array, array[index][5], code+'1')


def huffman(S, F):
    length = len(S)
    # inicjalizuja kolejki i zapis elementów do niej, zapisuję tablicę zawierającą częstotliwość występowania, nazwę,
    # kolejność z jaką elementy zostały podane i puste miejsce na string który później będzie zawierał kod Huffmana
    if length > 0:
        if length > 1:
            starting_array = PriorityQueue()
            for i in range(length):
                starting_array.put([F[i], S[i], i, ""])
            final_array = []
            index = 0

            # działamy tak długo jak w kolejce nie zostanie 1 element
            while starting_array.qsize() > 1:
                # dodaję do listy dwa elementy o najniższej częstotliwości występowania
                final_array.append(starting_array.get())
                final_array.append(starting_array.get())

                # jeśli w kolejce nie ma żadnego elementu, break, bo nie ma sensu dodawać ostatniego node jako pojedyńczego elementu
                if starting_array.empty():
                    break

                # dodaję do kolejki "node" o częstotliwości występowania równej sumie usuniętych elementów, dodaję także
                # indeksy "dzieci" tego node, na lewo i na prawo
                starting_array.put([final_array[index][0]+final_array[index+1][0], "node", 0, "", index+1, index+0])
                index += 2

            # wywołuję funkcję rekurencyjną dla dwóch ostatnich elementów listy, ponieważ nie zawiera ona ostatniego node
            # który miałby te dwa elementy jako swoje "dzieci"
            assigning(final_array, len(final_array)-1, '0')
            assigning(final_array, len(final_array)-2, '1')

            # sortuję listę po kolejności podania elementów i wypisuję, zliczając długość napisu
            sorter = lambda x: (x[2])
            final_array = sorted(final_array, key=sorter)
            counter = 0
            for i in range(len(final_array)):
                if final_array[i][1] != 'node':
                    print(final_array[i][1], ":", final_array[i][3])
                    counter += len(final_array[i][3])*final_array[i][0]
            print("dlugosc napisu:", counter)
        else:
            print(S[0], ": 0")
            print("dlugosc napisu:", F[0])


# S = ["a", "b", "c", "d", "e", "f"]
# F = [10, 11, 7, 13, 1, 20]

# S = ['a', 'b', 'c', 'd', 'e', 'f']
# F = [5, 9, 12, 13, 16, 45]
#
# S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']
# F = [27, 32, 123, 15, 4, 32, 23, 13, 44, 32, 12, 5, 3, 145, 54, 34, 98, 102, 76, 243, 45, 65, 78]

S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']
F = [27, 32, 123, 15, 4, 31, 23, 13, 44, 38, 12, 5, 3, 145, 54, 34, 98, 102, 76, 243, 45, 65, 78]

# S = ['a']
# F = [25]

start_time = time.time()
start = timeit.default_timer()
huffman(S, F)
stop = timeit.default_timer()
print("--- %s seconds ---" % (time.time() - start_time))
print(stop - start)