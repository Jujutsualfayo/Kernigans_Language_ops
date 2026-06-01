/*Adding fractions*/
#include <stdio.h>

int main(void){
    char name; int age, height; char result_xyz;
    printf("Whats your name? ");
    scanf("%c", &name);
    printf("Tell me your height: ");
    scanf("%d", &height);
    printf("Lastly your age sir: ");
    scanf("%d", &age);

result_xyz = name, age, height;
printf("Result of your answers of %c%d%d is: ", name, height, age);

return 0;
}
