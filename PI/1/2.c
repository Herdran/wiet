//Dana jest liczba całkowita dodatnia n. Napisz program, który znajduje wszystkie liczby
//pierwsze mniejsze od n, których cyfry tworzą ciąg niemalejący.
#include <stdio.h>

int is_prime(int num) {
    if (num == 2 || num == 3) {
        return 1;
    }
    if (num <= 1 || num % 2 == 0 || num % 3 == 0) {
        return 0;
    }

    int a = 5;
    while (a * a <= num) {
        if (num % a == 0) {
            return 0;
        }
        a += 2;
        if (num % a == 0) {
            return 0;
        }
        a += 4;
    }

    return 1;
}

int main(){
    int liczba;
    scanf("%d", &liczba);

    for (int i = 2; i < liczba; i++) {
        if (is_prime(i) == 1) {
            int copy = i;
            int prev = i;
            while (copy > 0 && copy % 10 <= prev) {
                prev = copy % 10;
                copy /= 10;
            }
            if (copy == 0) {
                printf("%d\n", i);
            }
        }
    }
    return 0;
}