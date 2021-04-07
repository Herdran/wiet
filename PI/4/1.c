#include <stdio.h>
#define MAX 158


int main() {
    int array[MAX];
    for (int i = 0; i < MAX - 1; i++) {
        array[i] = 0;
    }

    int n;
    scanf("%d", &n);

    array[MAX - 1] = 1;

    for (int i = 1; i <= n; i++){
        for (int j = MAX - 1; j >= 0; j--){
            array[j] *= i;
        }
        int index = MAX - 1;
        while (index > 0) {
            if (array[index] >= 10) {
                array[index - 1] += (array[index] / 10);
                array[index] = array[index] % 10;
            }
            else {
                index--;
            }
        }
    }

    int start = 0;
    while (array[start] == 0) {
        start++;
    }

    for (int i = start; i < MAX; i++) {
        printf("%d", array[i]);
    }

    return 0;
}