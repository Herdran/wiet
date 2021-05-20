#include <stdio.h>
#include <math.h>


int change_one_bit(int num, int k) {
    return (num ^ (1 << k));
}

int main() {
    int n;
    int len;
    int m;
    scanf("%d %d", &n, &m);

    len = pow(2, n);

    int counter = 0;
    int checked;
    for (int i = 1; i < len; i++){
        if (i % m != 0){
            for (int j = 0; j < n; j++){
                checked = change_one_bit(i, j);
                if (checked % m == 0 && checked != 0){
                    counter++;
                    j = n;
                }
            }
        }
    }

    printf("%d", counter);
    return 0;
}