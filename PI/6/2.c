#include <stdio.h>
#define size 12
char roman_numbers[3][size];
int numbers[1] = {0, 0};
char *symbols[13] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
int base[13] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};


int value(char val) {
    if (val == 'I') return 1;
    if (val == 'V') return 5;
    if (val == 'X') return 10;
    if (val == 'L') return 50;
    if (val == 'C') return 100;
    if (val == 'D') return 500;
    if (val == 'M') return 1000;
    return -1;
}


int main() {
    char tmp;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 12; j++) {
            scanf("%c", &tmp);
            if (tmp == ' ' || tmp == '\n') {
                j = 12;
            }
            else
                roman_numbers[i][j] = tmp;
        }
    }

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 12; j++) {
            int dig1 = value(roman_numbers[i][j]);
            if (dig1 != -1) {
                numbers[i] += dig1;
                int dig2 = value(roman_numbers[i][j + 1]);
                if (dig2 != -1) {
                    if (dig1 < dig2) {
                        numbers[i] += dig2;
                        numbers[i] -= (2 * dig1);
                        j++;
                    }
                }
            }
        }
    }

    int number = numbers[0]+numbers[1];
    int i = 12;
    while (number > 0) {
        int div = number / base[i];
        number = number % base[i];

        while (div > 0) {
            printf("%s", symbols[i]);
            div--;
        }
        i--;
    }

    return 0;
}
