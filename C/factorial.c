#include<stdio.h>
 int factorial(int );
int main()
{
    int i,fact,n;
    printf("enter the value of n");
    scanf("%d",&n);
    fact=factorial(n);
    printf(" factorial of %d is %d",n,fact);

}
 int factorial(int n)
{
    if (n==0)
        return 1;
    else if (n>0)
        return n*factorial(n-1);
}

