#include <stdio.h>


int is_prime(int num) {
    if (num == 2 || num == 3) {
        return 1;
    }
    if (num <= 1 || num % 2 == 0 || num % 3 == 0) {
        return 0;
    }

    int a = 5;
    while (a * a <= num) {
        if (num % a == 0) {
            return 0;
        }
        a += 2;
        if (num % a == 0) {
            return 0;
        }
        a += 4;
    }
    return 1;
}


int if_jednokwadratowa(int num) {
    int tmp;
    while (num != 1 && num != 4){
        tmp = 0;
        while (num > 0) {
            tmp += (num%10)*(num%10);
            num /= 10;
        }
        num = tmp;
    }

    if (num == 1){
        return 1;
    }
    return 0;
}


int main() {
    int l, u, k;
    int number = -1;
    scanf("%d %d %d", &l, &u, &k);

    for (int i = l; i<=u; i++){
        if (is_prime(i) == 1){
            if (if_jednokwadratowa(i) == 1){
                k -= 1;
                if (k == 0) {
                    number = i;
                    i = u + 1;
                }
            }
        }
    }

    printf("%d", number);
    return 0;
}
