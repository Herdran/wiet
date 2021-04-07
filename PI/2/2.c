#include <stdio.h>
#define MAX 8


int power(int a, int b) {
    int output = 1;
    for (int i = 1; i <= b; i++) {
        output *= a;
    }
    return output;
}

int main () {
    int m, b, digit, tmp, sum, index;
    char output[MAX], dig;
    scanf("%d %d", &m, &b);

    int down = power(b, m - 1);
    int up = power(b, m);
    int present = 0;

    for (int number = down; number < up; number++) {
        tmp = number;
        sum = 0;

        while (tmp > 0) {
            digit = tmp % b;
            sum += power(digit, m);
            tmp /= b;
        }

        if (sum == number) {
            present = 1;
            tmp = number;
            index = m - 1;
            while (tmp > 0) {
                digit = tmp % b;
                if (digit > 9) {
                    dig = 55 + digit;
                    output[index] = dig;
                }
                else {
                    dig = 48 + digit;
                    output[index] = dig;
                }
                tmp /= b;
                index--;
            }

            for (int i = 0; i < m; i++) {
                printf("%c", output[i]);
            }
            printf(" ");
        }
    }

    if (present == 0) {
        printf("NO");
    }

    return 0;
}