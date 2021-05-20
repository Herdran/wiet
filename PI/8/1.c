#include <stdio.h>

int array[20];


int main() {
    long long S;
    long long sum_ = 0;
    int length = 0;
    long long tmp;
    scanf("%lld", &S);

    while (sum_ < S){
        array[length] = 9;
        tmp = 1;
        for (int i = 0; i < length; i++){
            tmp = tmp*10+1;
        }
        sum_ += 9 * tmp;
        length++;
    }

    for (int i = length-1; i >= 0 ; i--){
        while (i < length-2 && array[i] > 0 || array[i] > 1){
            sum_ -= tmp;
            if (sum_ < S){
                sum_ += tmp;
                break;
            }
            array[i]--;
        }
        tmp /= 10;
    }

    if (sum_ == S) {
        for (int i = length - 1; i >= 0; i--) {
            printf("%d", array[i]);
        }
    }
    else{
        printf("-1");
    }
    return 0;
}