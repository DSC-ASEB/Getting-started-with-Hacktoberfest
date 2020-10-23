import java.util.Scanner;
import java.util.InputMismatchException;

public class Main {
    public static void main(String[] args) {
        int row;
        int i = 0, j = 0;
        boolean error = false;
        do {
            try {
                Scanner in = new Scanner(System.in);
                System.out.print("Enter rows for half of the diamond: ");
                row = in .nextInt();
                error = false;
                for (i = 0; i <= row; i++) {
                    for (j = 1; j <= row - i; j++)
                        System.out.print(" ");
                    for (j = 1; j <= 2 * i - 1; j++)
                        System.out.print("*");
                    System.out.print("\n");
                }
                for (i = row - 1; i >= 1; i--) {
                    for (j = 1; j <= row - i; j++)
                        System.out.print(" ");
                    for (j = 1; j <= 2 * i - 1; j++)
                        System.out.print("*");
                    System.out.print("\n");
                }
            } catch (InputMismatchException e) {
                System.out.println("Not a valid input, please try again.");
                error = true;
            }
        }
        while (error);
    }
}
