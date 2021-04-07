//Liczba doskonała jest to taka liczba naturalna, która jest sumą wszystkich swych dzielników właściwych (to znaczy od
//niej mniejszych). Najmniejszą liczbą doskonałą jest 6,
//ponieważ jej dzielnikami właściwymi są 1, 2, 3 i 1 + 2 + 3 = 6.
//Napisz program, który znajduje wszystkie liczby doskonałe w zadanym przedziale oraz
//ich liczbę.


#include <stdio.h>

int main(){
    int start;
    int end;

    scanf("%d %d", &start, &end);

    if (start == 1){
        start ++;
    }
    int counter = 0;
    for (int i = start; i <= end; i++) {
        int sum = 1;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                sum += j + i / j;
            }
        }
        if (sum == i)
            counter ++;
    }

    printf("%d\n", counter);
    while (counter > 0){
        for (int i = start; i <= end; i++) {
            int sum = 1;
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    sum += j + i / j;
                }
            }
            if (sum == i)
                printf("%d ", sum);
                counter --;
        }
    }
    return 0;
}