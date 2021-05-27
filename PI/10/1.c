#include <stdio.h>
#include <stdlib.h>


int xor(int f1, int f2){
    if ((f1 == 1 && f2 == 0) || (f1 == 0 && f2 == 1)){
        return 1;
    }
    return 0;
}


int main() {
    int n, m, end;
//    int aa, bb;
    scanf("%d %d %d", &n, &m, &end);
    end --;
    int **array = (int **) malloc(m * sizeof(int *));
    for (int i = 0; i < m; i++) {
        array[i] = (int *) malloc(2 * sizeof(int));
    }


    int *num = (int *) malloc(n * sizeof(int));
    int *top_n = (int *) malloc(n * sizeof(int));
    char *bot = (char *) malloc(n * sizeof(char));
    char *top = (char *) malloc(n * sizeof(char));


    int *xorarr = (int *) malloc(m * sizeof(int));

    for (int i = 0; i < m; i++) {
        scanf("%d %d", &array[i][0], &array[i][1]);
    }
    scanf("%s", bot);
    scanf("%s", top);
    for (int i = 0; i < n; i++) {
        num[i] = ((int) bot[i]) - 48;
        top_n[i] = ((int) top[i]) - 48;
    }


    int counter, f1, f2;
    int bigcount = 0;
    int check = 1;
    while (check != 0){
        for (int i = 0; i < m; i++) {
            xorarr[i] = 2;
        }
        counter = 0;
        while (counter < m){
            for (int i = 0; i < m; i++){
                if (xorarr[i] == 2){
                    f1 = array[i][0];
                    f2 = array[i][1];
                    if (f1 < 0){
                        f1 = num[-f1-1];
                    }
                    else{
                        f1 = xorarr[f1-1];
                        if (f1 == 2){
                            continue;
                        }
                    }
                    if (f2 < 0){
                        f2 = num[-f2-1];
                    }
                    else{
                        f2 = xorarr[f2-1];
                        if (f2 == 2){
                            continue;
                        }
                    }
                    xorarr[i] = xor(f1, f2);
                    counter += 1;
                }
            }
        }

        if (xorarr[end] == 1){
            bigcount++;
        }
        for (int i = n - 1; i >= 0; i--){
            if (num[i] == 0){
                num[i] = 1;
                i = -1;
            }
            else{
                num[i] = 0;
            }
        }
        if (check == 2){
            check = 0;
        }
        else{
            for (int i = 0; i < n; i++){
                if (num[i] != top_n[i]){
                    check = 1;
                    break;
                }
                check = 2;
            }
        }

    }
    printf("%d", bigcount);

    return 0;
}
