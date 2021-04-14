#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    int k;
    scanf("%d %d", &n, &k);
    int counter = 0;
    char tmp;


    int **T = (int **)malloc(n * sizeof(int *));
    int **results = (int **)malloc((n * n - (4 * n) + 4) * sizeof(int *));
    for (int i = 0; i < n; i++) {
        T[i] = (int *)malloc(n * sizeof(int));
    }
    for (int i = 0; i < n * n; i++) {
        results[i] = (int *)malloc(2 * sizeof(int));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d%c", &T[i][j], &tmp);
        }
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            for (int size = 1; size < n; size++) {
                if ((i - size < 0) || (j - size < 0) || (i + size >= n) || (j + size) >= n) {
                    size = n;
                }
                else {
                    int sum = 0;
                    for (int x = j - size; x <= j + size; x++) {
                        sum += T[i - size][x];
                        sum += T[i + size][x];
                    }
                    for (int y = (i - size) + 1; y < i + size; y++) {
                        sum += T[y][j - size];
                        sum += T[y][j + size];
                    }
                    if (sum == k) {
                        results[counter][0] = i;
                        results[counter][1] = j;
                        counter++;
                    }
                }
            }
        }
    }

    printf("%d\n", counter);
    for (int i = 0; i < counter; i++) {
        printf("%d %d\n", results[i][0], results[i][1]);
    }

    return 0;
}