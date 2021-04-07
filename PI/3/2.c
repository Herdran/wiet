#include <stdio.h>
#include <stdlib.h>

int cmpfunc (const void * a, const void * b) {
    return ( *(int*)a - *(int*)b );
}


int main() {
    int n,k;
    int counter = 0;
    int flag = 0;
    int j;
    scanf("%d %d",&n,&k);

    int* array = (int*) calloc(n, sizeof(int));

    for(int i=0;i<n;i++){
        scanf("%d",&array[i]);
    }


    if (n > 0) {
        qsort(array, n, sizeof(int), cmpfunc);
        for (int i = 0; i < n; i++) {
            if (i == 0 || array[i - 1] != array[i]) {
                flag = 0;
                if (i < n - 1) {
                    j = i + 1;
                    while (j < n - 1 && array[j] == array[i]) {
                        j++;
                    }
                    if (array[j] <= array[i] + k && array[i] != array[j]) {
                        flag = 1;
                    }
                }
                if (i > 0 && flag == 0) {
                    j = i - 1;
                    while (j > 0 && array[j] == array[i]) {
                        j--;
                    }
                    if (array[j] >= array[i] - k && array[i] != array[j]) {
                        flag = 1;
                    }
                }
            }
            if (flag == 1) {
                counter++;
            }
        }
    }
    printf("%d", counter);
    return 0;
}
