#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    int counter = 0;
    int border = 0;
    scanf("%d", &n);

    int **F = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        F[i] = (int *)malloc(n * sizeof(int));
    }

    while (counter < n * n) {
        for (int i = border; i < n - border; i++) {
            counter++;
            F[border][i] = counter;
        }
        for (int i = border + 1; i <= n - (border + 1); i++) {
            counter++;
            F[i][(n - 1) - border] = counter;
        }
        for (int i = n - 2 - border; i >= border; i--) {
            counter++;
            F[(n - 1) - border][i] = counter;
        }
        for (int i = (n - 1) - (border + 1); i > border; i--) {
            counter++;
            F[i][border] = counter;
        }
        border++;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", F[i][j]);
        }
        printf("\n");
    }

    return 0;
}