/*

Just having fun

Don't blame me for that

I learn all the time :)

*/

#include <stdlib.h>


void inm()
{
int i,j,rez;
    for (i = 1; i <= 9; i++)
    {
        for (j = 1; j <=9; j++)
        {
        rez = i * j;
        printf("%d * %d = %d \n",i,j,rez);
        }
    }
}

void nume()
{
    char nume[10];
    puts("Introdu numele tau: ");
    scanf("%s",nume);
    printf("Numele tau este : %s\n");
}
int main()
{
    int choice;
    do {
    printf("<<<<<<<<<<<<<<<<    MENIU   >>>>>>>>>>>>>>>>>>      \n");
    printf("1. Tabla inmultirii\n");
    printf("2. Numele tau \n");
    printf("3. Parole si salvare\n");
    printf("4.\n");
    printf("5. Iesire\n");
    scanf("%d",&choice);
    switch(choice)
        {
        case 1: inm();
        break;
        case 2: nume();
        break;
        default:
            printf("Goodbye my friend! \n");

        break;
        }
    } while (choice != 5);
return 0;

}
