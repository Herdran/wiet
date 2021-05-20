#include <stdio.h>
#include <stdlib.h>


int g[30];
int candidates[20][30];
int blacklist[30];
int counter_arr[30];

int main() {
    int n;
    int G;
    scanf("%d %u", &n, &G);

    int *T = (int *) malloc(n * sizeof(unsigned int));
    int *cands = (int *) malloc(n * sizeof(unsigned int));

    for (int i = 0; i < n; i++) {
        scanf("%u", &T[i]);
    }

    int ind = 0;
    for (int i = 0; i < n; i++) {
        if ((T[i] | G) == G) {
            cands[ind] = T[i];
            ind++;
        }
    }

    int tmp = 1;
    int counter = 1;
    while (G > tmp){
        tmp *= 2;
        counter++;
    }
    if (tmp > 1){
        counter--;
    }
    int index = 0;

    for (int i = counter-1; i >=0; i--){
        g[i] = G%2;
        G /= 2;
        if (g[i] == 0){
            blacklist[index] = i;
            index++;
        }
        for (int j = 0; j < ind; j++){
            candidates[j][i] = cands[j]%2;
            cands[j] /= 2;
        }
    }


    int flag = 0;

    for (int i = 0; i < counter; i++){
        if (g[i] == 1){
            for (int j = 0; j < ind; j++){
                if (candidates[j][i] == 1){
                    counter_arr[i]++;
                    flag = 1;
                    for (int l = 0; l < index; l++){
                        if (candidates[j][blacklist[l]] == 1){
                            counter_arr[i]--;
                            break;
                        }
                    }
                }
            }
        }
    }


    if (flag == 0){
        printf("%d", 0);
        return 0;
    }

    int min = ind;
    for (int i = 0; i < counter; i++){
        if (counter_arr[i] < min && counter_arr[i] != 0){
            min = counter_arr[i];
        }
    }

    printf("%d", min);
    return 0;
}