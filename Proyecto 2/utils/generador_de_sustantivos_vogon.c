#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(){
    int i = 70;
    char str[] = "";
    while (i != 0)
    {
        char a = (char)(rand() % ('z' - 'a') + 'a');
        char b = (char)(rand() % ('z' - 'a') + 'a');
        char c = (char)(rand() % ('z' - 'a') + 'a');
        char d = (char)(rand() % ('z' - 'a') + 'a');
        char e = (char)(rand() % ('z' - 'a') + 'a');

        printf("%c%c%c%c%c%c ", a, 'a', c, 'e', e, 'o');
        i--;
    }
}