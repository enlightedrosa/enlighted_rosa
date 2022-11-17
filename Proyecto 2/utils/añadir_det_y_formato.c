#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int ft_tildesyeñes(char *str)
{
    int i = 0;
    while(str[i])
    {
        if (isalnum(str[i]) == 0)
            return (0);
        i++;
    }
    return (1);
}


int main(int argc, char **argv){
    printf(" argc == %i\n", argc);
    argc--;
    int i = 0;
    while(argc >= 0)
    {
        int a = strlen(argv[argc]) - 1;
        if (ft_tildesyeñes(argv[argc])){
            if (argv[argc][a] == 'o'){
                printf("\"el ");
                printf("%s\", ", argv[argc]);
            } else if (argv[argc][a] == 's'){
                if (argv[argc][a - 1] == 'o'){
                    printf("\"los ");
                    printf("%s\", ", argv[argc]);
                } else if (argv[argc][a - 1] == 'a'){
                    printf("\"las ");
                    printf("%s\", ", argv[argc]);
                }
            } else if (argv[argc][a] == 'a'){
                printf("\"la ");
                printf("%s\", ", argv[argc]);
            }
            i++;
        }
        argc--;
    }
    printf("\n--- args --- %i \n", i);
    return (0);
}