#include <stdio.h>
#define size 200

int main() {
    char tmp;
    int n;
    int counter = 0;
    scanf("%d", &n);
    int plane[size][size];
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            plane[i][j] = 0;
        }
    }

    int **array = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++){
        array[i] = (int * )malloc(4 * sizeof(int *));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%d%c", &array[i][j], &tmp);
        }
    }

    for (int z = 0; z < n; z++){
        for (int i = array[z][0]+100; i < array[z][2]+100; i++){
            for (int j = array[z][1]+100; j < array[z][3]+100; j++){
                if (plane[i][j] == 0){
                    plane[i][j] = 1;
                    counter++;
                }
                else {
                    plane[i][j] = 0;
                    counter--;
                }
            }
        }
    }
    printf("%d", counter);

    return 0;
}