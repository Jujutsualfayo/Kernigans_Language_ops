#include <stdio.h>

int main(void)
{
    char full_name[100];

    printf("Enter your full name: ");

    fgets(full_name, sizeof(full_name), stdin);

    printf("Welcome %s", full_name);

    return 0;
}
