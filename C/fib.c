/*Recusion + memorization is called dyanamic programing*/
#include<stdio.h>
main()
{
    int n,p;//m[1000];
    scanf("%d",&n);
    p=fib(n);
    printf("%d",p);
}
fib(int n)
{
 int m[1000];
if (n==0)
m[1]=0;
else if(n==1)
m[2]=1;
else if(m[n]==0)
m[n]=fib(n-2)+fib(n-1);
return m[n];
}
