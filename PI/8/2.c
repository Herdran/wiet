#include <stdio.h>


int main() {
    int N;
    long long sum_ = 0;
    int counter;
    int j;
    scanf("%ld", &N);

    for (int i = 1; i <=N; i+=2){
        counter = 1;
        j = 2;
        while (i*j <= N){
            j*=2;
            counter++;
        }
        sum_ += i*counter;
    }

    printf("%lld", sum_);
    return 0;
}


//#pragma GCC optimize("Ofast")
//#pragma GCC optimize("unroll-loops")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma,tune=native")
//#include <stdio.h>
//
//
//int main() {
//    long N;
//    long long sum_ = 0;
//    scanf("%ld", &N);
//
//    for (long i = 1; i <=N; i++){
//        sum_ += i >> __builtin_ctz(i);
//    }
//
//    printf("%lld", sum_);
//    return 0;
//}