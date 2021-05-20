#include <stdio.h>
#include <string.h>


int array[50];


int main() {
    char string[50], current, compared;

    int t, position = 0;
    gets(string);
    t = strlen(string);


    while (position < t) {
        compared = string[position];
        for (int i = position; i < t; i++) {
            current = string[i];
            if (current > compared){
                compared = current;
                position = i;
            }
        }
        array[position] = 1;
        position ++;
    }
    for (int i = 0; i < 50; i++){
        if (array[i] == 1){
            printf("%c", string[i]);
        }
    }
    return 0;
}