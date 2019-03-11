#include <stdio.h>
#include "ninstances-c/ninstances.h"

int main(void)
{
int x, flag;
flag=1;

while(flag==1)
{
printf("Menu:\n");
printf("0.- EXIT\n");
printf("1.- Number of instances, features and labels (Juan A. Romero)\n");
printf("2.- Mean of the values of each instance (Angel Murcia)\n");
scanf("%d", &x);
fflush(stdin);
printf("\n\n");
switch(x){
    case 0:
        flag=0;
        break;
    case 1:
        printf("Ejecutando la función ninstances() de Juan A. Romero:\n");
        ninstances("yeast.complete");
        break;
    case 2:
        printf("Ejecutando para dar la media numerica de todas las variables de cada instancia de Angel Murcia\n");
        mifuncion("yeast.complete");
        break;
/* add here more functionality */
    }
}

}
