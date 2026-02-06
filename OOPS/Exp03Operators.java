/*
Experiment 03: Operators in Java
Objective:
- Apply different types of operators to perform arithmetic, comparison,
  logical decisions, and more.

Run:
    javac Exp03Operators.java
    java Exp03Operators
*/

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Exp03Operators {
    public static void main(String[] args) {
        System.out.println("Experiment 03: Operators in Java");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter integer a (e.g., 10): ");
        if (!sc.hasNextInt()) {
            System.out.println("Invalid input. Please enter integers.");
            sc.close();
            return;
        }
        int a = sc.nextInt();

        System.out.print("Enter integer b (e.g., 3): ");
        if (!sc.hasNextInt()) {
            System.out.println("Invalid input. Please enter integers.");
            sc.close();
            return;
        }
        int b = sc.nextInt();

        System.out.println("\nArithmetic operators:");
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        if (b != 0) {
            System.out.println("a / b = " + (a / b));
            System.out.println("a % b = " + (a % b));
        } else {
            System.out.println("Division operations skipped (b is 0)." );
        }
        System.out.println("a++ = " + (a++));
        System.out.println("++a = " + (++a));

        System.out.println("\nComparison operators:");
        System.out.println("a == b -> " + (a == b));
        System.out.println("a != b -> " + (a != b));
        System.out.println("a < b  -> " + (a < b));
        System.out.println("a <= b -> " + (a <= b));
        System.out.println("a > b  -> " + (a > b));
        System.out.println("a >= b -> " + (a >= b));

        System.out.println("\nLogical operators:");
        boolean cond1 = a > 0;
        boolean cond2 = b > 0;
        System.out.println("(a > 0) && (b > 0) -> " + (cond1 && cond2));
        System.out.println("(a > 0) || (b > 0) -> " + (cond1 || cond2));
        System.out.println("!(a > 0)           -> " + (!cond1));

        System.out.println("\nBitwise operators:");
        System.out.println("a & b  = " + (a & b));
        System.out.println("a | b  = " + (a | b));
        System.out.println("a ^ b  = " + (a ^ b));
        System.out.println("~a     = " + (~a));
        System.out.println("a << 1 = " + (a << 1));
        System.out.println("a >> 1 = " + (a >> 1));

        System.out.println("\nAssignment operators:");
        int x = a;
        x += b;
        System.out.println("x = a; x += b -> " + x);
        x = a;
        x *= b;
        System.out.println("x = a; x *= b -> " + x);

        System.out.println("\nMembership (via List.contains) and identity:");
        List<Integer> items = Arrays.asList(a, b, a + b);
        System.out.println("List: " + items);
        System.out.println("a in list -> " + items.contains(a));
        System.out.println("999 not in list -> " + !items.contains(999));

        List<Integer> y = items;
        List<Integer> z = Arrays.asList(a, b, a + b);
        System.out.println("y == items -> " + (y == items));
        System.out.println("z == items -> " + (z == items));
        System.out.println("z.equals(items) -> " + z.equals(items));

        sc.close();
    }
}
