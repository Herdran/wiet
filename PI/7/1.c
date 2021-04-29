#include <stdio.h>
#include <stdlib.h>
#define SIZE 65

long amount[SIZE];

int main() {
    long k;
    int n;

    scanf("%d %ld", &n, &k);
    amount[0] = 1;
    amount[1] = 2;

    for (int i = 2; i < 65; i++) {
        amount[i] = amount[i - 1] + amount[i - 2];
    }


    if (k > amount[n]) {
        printf("-1");
        return 0;
    }
    int **array = (int **) malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++){
        array[i] = 0;
    }

    for (int i = 0; i < k-1; i++){
        for (int j = n-1; j >= 0; j--) {
            if (array[j] == 0 && (j == 0 || array[j-1] == 0)){
                array[j] = 1;
                for (int z = j+1; z < n; z++){
                    array[z] = 0;
                }
                j = -1;
            }
            else {
                if (array[j-1] == 0 && array[j-2] == 0){
                    array[j] = 0;
                }
            }
        }
    }
    for (int i = 0; i < n; i++){
        printf("%d", array[i]);
    }
    return 0;
}
