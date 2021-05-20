#include <stdio.h>
#include <stdlib.h>


int max(int a, int b) {
    if (a > b) return a;
    return b;
}

int main() {
    int n, k, l, result = 0;
    int current = 0;
    scanf("%d %d %d", &n, &k, &l);
    char tmp;

    int **array1 = (int **) malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        array1[i] = (int *) malloc(n * sizeof(int));
    }
    int **array2 = (int **) malloc(k * sizeof(int *));
    for (int i = 0; i < k; i++) {
        array2[i] = (int *) malloc(l * sizeof(int));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d%c", &array1[i][j], &tmp);
        }
    }
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < l; j++) {
            scanf("%d%c", &array2[i][j], &tmp);
        }
    }


    for (int i = 0; i < n-k; i++) {
        for (int j = 0; j < n-l; j++) {
            current = 0;
            for (int x = 0; x < k; x++) {
                for (int y = 0; y < l; y++) {
                    if (array2[x][y] == 1) {
                        current += array1[i + x][j + y];
                    }
                }
            }
            result = max(result, current);
        }
    }


    printf("%d", result);
    return 0;
}