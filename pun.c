/*Adding fractions*/
#include <stdio.h>

int main(void){
    char name[50]; int age; float height; 
    printf("Whats your name? ");
    scanf("%s", &name);
    printf("Tell me your height: ");
    scanf("%f", &height);
    printf("Lastly your age sir: ");
    scanf("%d", &age);

    printf("\nName: %s\n", name);
    printf("Height: %.2f\n", height);
    printf("Age: %d\n", age);

    return 0;
}
