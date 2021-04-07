//Mamy dany zestaw n odważników o masach danych liczbami naturalnymi. Napisz program, który sprawdza, czy zadany ciężar
//w można zważyć przy pomocy wagi dwuszalkowej (czyli odważniki mogą być po obu stronach wagi).

#include <stdio.h>
#define MAX 100

int scale (int array[MAX], int mass, int index, int amount) {
    if (index > amount) {
        return 0;
    }
    if (mass == 0) {
        return 1;
    }
    return scale(array, mass - array[index], index + 1, amount) || scale(array, mass, index + 1, amount) ||
           scale(array, mass + array[index], index + 1, amount);
}


int main() {
    int amount;
    int mass;
    int i=0;
    int sum=0;
    scanf("%d %d", &amount, &mass);
    int array[MAX];
    char temp;

    while(temp != '\n'){
        scanf("%d%c", &array[i], &temp);
        sum+=array[i];
        i++;
    }

    if (sum < mass){
        printf("NO");
        return 0;
    }
    if (sum == mass){
        printf("YES");
        return 0;
    }
    if (scale(array, mass, 0, amount) == 1) {
        printf("YES");
    }
    else {
        printf("NO");
    }
    return 0;
}
