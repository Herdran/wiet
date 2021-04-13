#include <stdio.h>
#include <stdlib.h>


int main () {
    int n;
    int x = 0;
    int y = 0;
    int max_width;
    int max_height;
    int width_res;
    int height_res;
    int stop;
    char tmp;
    scanf("%d", &n);
    int **F = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        F[i] = (int *)malloc(n * sizeof(int));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d%c", &F[i][j], &tmp);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            max_width = 0;
            max_height = 0;
            for (int width = j; width <= n; width++){
                if (width == n || F[i][width] == 1){
                    max_width = width-j;
                    width = n;
                }
            }
            while (max_width > 0){
                stop = 0;
                while (stop == 0 && max_width*n > x*y) {
                    for (int height = i; height <= n; height++) {
                        for (int width = j; width < max_width+j; width++) {
                            if (height == n || F[height][width] == 1) {
                                stop = 1;
                                height_res = height;
                                width = n;
                                height = n;
                            }
                        }
                    }
                    if ((height_res-i) * max_width > x * y) {
                        x = height_res-i;
                        y = max_width;

                    }
                }
                max_width--;
            }
            for (int height = i; height <= n; height++){
                if (height == n || F[height][j] == 1){
                    max_height = height-i;
                    height = n;
                }
            }
            while (max_height > 0){
                stop = 0;
                while (stop == 0 && max_height*n > x*y) {
                    for (int width = j; width <= n; width++) {
                        for (int height = i; height < max_height+i; height++) {
                            if (width == n || F[height][width] == 1) {
                                stop = 1;
                                width_res = width;
                                width = n;
                                height = n;
                            }
                        }
                    }
                    if (max_height * (width_res-j) > x * y) {
                        x = max_height;
                        y = width_res-j;
                    }
                }
                max_height--;
            }
        }
    }


    printf("%d", (x)*(y));

    return 0;
}