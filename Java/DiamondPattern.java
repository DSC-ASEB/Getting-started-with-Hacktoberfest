import java.util.Scanner;
import static java.lang.System.exit;

public class DiamondPattern {
  public static void main(String[] args) {
   int row ;
   int i =0 , j = 0 ;
   Scanner in = new Scanner(System.in);
   for (;;) {
    System.out.print("Enter rows for half of the diamond : ");     
		   row = in.nextInt();
		    if (row >= 1) {
   for(i=0;i<=row;i++)
   {
     for(j=1;j<=row-i;j++)
     System.out.print(" ");
     for(j=1;j<=2*i-1;j++)
       System.out.print("*");
     System.out.print("\n");
   }
 
   for(i=row-1;i>=1;i--)
   {
     for(j=1;j<=row-i;j++)
     System.out.print(" ");
     for(j=1;j<=2*i-1;j++)
       System.out.print("*");
     System.out.print("\n");
   }
            }else{
         System.out.println("Wrong Input");
                exit(1);
            }
}
}
}
