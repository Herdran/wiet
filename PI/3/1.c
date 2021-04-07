#include <stdio.h>
#include <stdlib.h>

int cmpfunc (const void * a, const void * b) {
    return ( *(int*)b - *(int*)a );
}


int main() {
    int n;
    int k;
    scanf("%d %d", &n, &k);
    int array[n];
    char temp;
    int sum=0;
    int x;
    int tmp;

    for (int i = 0; i < n; i++){
        scanf("%d%c", &array[i], &temp);
        sum += array[i];
    }

    if (n == 1){
        int x = array[0];
        while (k > 0 && sum > 0){
            sum -= x - x/2;
            x = x/2;
            k -= 1;

        }
    }

    else {
        qsort(array, n, sizeof(int), cmpfunc);
        while (k > 0 && sum > 0) {
            while (array[0] >= array[1] && array[0] != 0 && k > 0){
                sum -= array[0] - array[0] / 2;
                array[0] = array[0] / 2;
                k -= 1;
            }
            x = 0;
            while (array[x] < array[x+1] && x < n - 1){
                tmp = array[x];
                array[x] = array[x+1];
                array[x+1] = tmp;
                x += 1;
            }
        }
    }
    printf("%d", sum);
    return 0;
}
