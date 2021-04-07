#include <stdio.h>


int main() {
    char tmp;
    int n;
    scanf("%d", &n);

    int **array = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++){
        array[i] = (int * )malloc(n * sizeof(int *));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d%c", &array[i][j], &tmp);
        }
    }

    int *t2 = (int *)malloc((n * n) * sizeof(int));
    int *indexes = (int *)malloc((n * n) * sizeof(int));

    for (int i = 0; i < n*n; i++) {
        t2[i] = 0;
        indexes[i] = 0;
    }
    int min_val = -1;
    int index = 0;
    int index_of_min_val = 0;
    for (int i = 0; i < n*n; i++){
        min_val = -1;
        for (int j = 0; j < n; j++){
            if (indexes[j] < n) {
                if (min_val == -1 || array[j][indexes[j]] < min_val) {
                    min_val = array[j][indexes[j]];
                    index_of_min_val = j;
                }
            }
        }
        if (index == 0 || t2[index-1] < min_val){
            t2[index] = min_val;
            index++;
        }
        indexes[index_of_min_val]++;
    }

    for (int i = 0; i < index; i++) {
        printf("%d ", t2[i]);
    }

    return 0;
}