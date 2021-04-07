//Napisz program, który dla zadanej liczby naturalnej n odpowiada na pytanie, czy liczba
// ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego. Zakładamy,
//że pierwsze dwa wyrazy ciągu Fibonacciego to 0 i 1.

#include <stdio.h>

int main(){
    int liczba;
    int n1 = 0;
    int n2 = 1;
    scanf("%d", &liczba);
    while (n1 * n2 < liczba){
        n2 = n1 + n2;
        n1 = n2 - n1;
    }
    if (n1 * n2 == liczba) {
        printf ("YES");
    }
    else {
        printf("NO");
    }
    return 0;
}