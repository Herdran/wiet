#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    int m;
    int counter = 0;
    scanf("%d %d", &n, &m);
    int t = (n * (n - 1) * (n - 2)) / 6;


    int **array_of_lines = (int **) malloc(m * sizeof(int *));
    for (int i = 0; i < m; i++) {
        array_of_lines[i] = (int *) malloc(2 * sizeof(int));
    }

    int **array_of_triangles = (int **) malloc(t * sizeof(int *));
    for (int i = 0; i < t; i++) {
        array_of_triangles[i] = (int *) malloc(4 * sizeof(int));
    }
    int *colors = (int *) malloc(t * sizeof(int));

    int triangle = 0;
    for (int i = 1; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            for (int l = j + 1; l <= n; l++) {
                array_of_triangles[triangle][0] = i;
                array_of_triangles[triangle][1] = j;
                array_of_triangles[triangle][2] = l;
                triangle++;
            }
        }
    }

    for (int i = 0; i < t; i++){
        colors[i] = 0;
    }

    for (int i = 0; i < m; i++) {
        scanf("%d %d", &array_of_lines[i][0], &array_of_lines[i][1]);
    }

    for (int i = 0; i < m; i++) {
        int x = array_of_lines[i][0], y = array_of_lines[i][1];
        for (int j = 0; j < t; j++) {
            if ((array_of_triangles[j][0] == x && array_of_triangles[j][1] == y) || (array_of_triangles[j][0] == x && array_of_triangles[j][2] == y) ||
                (array_of_triangles[j][1] == x && array_of_triangles[j][2] == y)) {
                colors[j]++;
            }
        }
    }

    for (int i = 0; i < t; i++) {
        if (colors[i] == 0 || colors[i] == 3) {
            counter++;
        }
    }

    printf("%d", counter);
    return 0;
}