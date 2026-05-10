/*Adding fractions*/

int main(void){
    int numb1, numb2, denom1, denom2, result_num, result_denom;
    printf("Input first fraction: ");
    scanf("%d/%d", &numb1, &denom1);
    printf("Input second fraction: ");
    scanf("%d/%d", &numb2, &denom2);
    
    result_num = numb1 * denom2 + numb2 * denom1;
    result_denom = denom1 * denom2;
    printf("Sum of the fraction is %d/%d\n", result_num, result_denom);

    return 0;
}
    