//Napisz program, który przyjmuję tablicę liczb naturalnych i zwraca taki indeks, że sumy
//wartości elementów tablicy na lewo i na prawo od wyznaczonego miejsca są równe. Można
//założyć, że rozwiązanie istnieje.

#include <stdio.h>

int main() {
    int length;
    int i=0;
    scanf("%d", &length);
    int array[length];
    char temp;
    do {
        scanf("%d%c", &array[i], &temp);
        i++;
    } while(temp != '\n');

    int center = (length/2);
    int sum_l=0,sum_r=0;
    if (length == 1) {
        printf("%d", 0);
    }
    else {
        for (int i = 0; i<center;i++) {
            sum_l += array[i];
        }
        for (int i = length-1; i>center;i--) {
            sum_r += array[i];
        }
        while(sum_l>sum_r) {
            sum_r += array[center];
            center--;
            sum_l -=array[center];
        }
        while(sum_l<sum_r) {
            sum_l += array[center];
            center++;
            sum_r -=array[center];
        }
        printf("%d", center);
    }
    return 0;
}
