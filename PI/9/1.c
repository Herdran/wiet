#include <stdio.h>
#include <string.h>

char s[50];
int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
char strings[2500][50];

int main() {
    int n;
    scanf("%s", s);

    for (int i = 0; i < 50; i++) {
        if (s[i] == '\0') {
            break;
        }
        n++;
    }

    int index = 0;
    for (int o = 0; o < n; o++) {
        for (int p = 0; p < 15; p++) {
            if (primes[p] < n) {
                for (int i = 0; i < n; i++) {
                    strings[index][i] = s[(o + i * primes[p]) % n];
                }
                index++;
            }
        }
    }

    int smallest = 0;
    for (int i = 1; i < 2500; i++) {
        if (strings[i][0] != '\0') {
            if (strcmp(strings[i], strings[smallest]) == -1) {
                smallest = i;
            }
        }
    }

    printf("%s", strings[smallest]);

    return 0;
}