#include <stdio.h>
#include <stdlib.h>


int main () {
    int n;
    int r;
    char tmp;
    scanf("%d %d", &n, &r);

    int **F = (int **)malloc(n * sizeof(int *));
    int **W = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        F[i] = (int *)malloc(n * sizeof(int));
        W[i] = (int *)malloc(n * sizeof(int));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {

            scanf("%d%c", &F[i][j], &tmp);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int sum = 0;
            for (int a = (i - r); a <= (i + r); a++) {
                if ((a >= 0) && (a < n)){
                    for (int b = (j - r); b <= (j + r); b++) {
                        if ((b >= 0) && (b < n)) {
                            sum += F[a][b];
                        }
                    }
                }
            }
            W[i][j] = sum;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", W[i][j]);
        }
        printf("\n");
    }

    return 0;
}