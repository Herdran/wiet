#include <stdio.h>
#include <stdlib.h>


int max(int a, int b) {
    if (a > b) return a;
    return b;
}

int main() {
    int n, k;
    int counter1, counter2, counter3, counter4, result = 0;
    scanf("%d %d", &n, &k);
    char tmp;
    int len = n+k;
    int **array = (int **) malloc(len * sizeof(int *));
    for (int i = 0; i < len * 3; i++) {
        array[i] = (int *) malloc(len * sizeof(int));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d%c", &array[i][j], &tmp);
        }
    }

    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            array[i + n][j + n] = array[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++) {
            array[i][j + n] = array[i][j];
        }
    }
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < k; i++) {
            array[i + n][j] = array[i][j];
        }
    }

//    for (int i = 0; i < len; i++) {
//        for (int j = 0; j < len; j++) {
//            printf("%d ", array[i][j]);
//        }
//        printf("\n");
//    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            counter1 = 0;
            counter2 = 0;
            counter3 = 0;
            counter4 = 0;
            for (int z = 0; z < k; z++){
                if (counter1 != -1 && j+z < len-1 && array[i][j+z] != 0){
                    counter1 += array[i][j+z];
                }
                else{
                    counter1 = -1;
                }
                if (counter2 != -1 && i+z < len-1 && array[i+z][j] != 0){
                    counter2 += array[i+z][j];
                }
                else{
                    counter2 = -1;
                }
                if (counter3 != -1 && i+z < len-1 && j+z < len && array[i+z][j+z] != 0){
                    counter3 += array[i+z][j+z];
                }
                else{
                    counter3 = -1;
                }
                if (counter4 != -1 && i+z < len-1 && j-z >= 0 && array[i+z][j-z] != 0){
                    counter4 += array[i+z][j-z];
                }
                else{
                    counter4 = -1;
                }
            }
            result = max(result, (max(counter1, max(counter2, max(counter3, counter4)))));
        }
    }

    printf("%d", result);

    return 0;
}