#include<stdio.h>
int maxheapfy( int a[], int);
int adjust(int a[],int i,int n);
int heapsort(int a[],int n);
int exchange(int* , int* );
int exchange( int* p, int* q)
/**********************************************/
{
    int temp;
    temp=*p;
    *p=*q;
    *q=temp;
}
/**********************************************/
int heapsort(int a[],int n)
{
    int j,i;
 maxheapfy(a ,n);
    {
        for(j=n;j>=2;j--)
        {
            exchange(&a[1],&a[j]);
            adjust(a,1,j-1);
        }
    }
}
/**********************************************/
int adjust(int a[],int i,int n)
{
    int j;
        while(2*i<=n)
        {
            j=2*i;
            if(j+1<=n)
            {
               if(a[j+1]>a[j])
               {
                   j=j+1;
               }
            }

            if(a[j]>a[i])
               {
                   exchange(&a[j],&a[i]);
               }

            else
                break;
            i=j;
        }
}
/**********************************************/
int maxheapfy(int a[], int n)
{
        int i;
        for(i=n/2;i>=1;i--)
        {
          adjust(a,i,n);
        }
}
/**********************************************/
int main()
{
    int i,n,a[10];
    printf("enter the no of element");
    scanf("%d",&n);
    printf("enter the element");
    for(i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    heapsort(a,n);
    printf("heap sort");
    for(i=1;i<=n;i++)
    {
        printf(" %d ",a[i]);
    }
}
/**********************************************/

