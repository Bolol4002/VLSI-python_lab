/*
Experiment 01: Decision-making and Loops
Objective:
- Implement business logic using combinations of decision-making and loops.

Run:
    javac Exp01DecisionLoops.java
    java Exp01DecisionLoops
*/

import java.util.Scanner;

public class Exp01DecisionLoops {
    static long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("factorial is not defined for negative numbers");
        }
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    static int sumOfDigits(int n) {
        n = Math.abs(n);
        int total = 0;
        while (n > 0) {
            total += n % 10;
            n /= 10;
        }
        return total;
    }

    static String describeNumber(int n) {
        String sign = (n > 0) ? "positive" : (n < 0) ? "negative" : "zero";
        String parity = (n % 2 == 0) ? "even" : "odd";
        return n + " is " + sign + " and " + parity + ".";
    }

    public static void main(String[] args) {
        System.out.println("Experiment 01: Decision-making and Loops");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an integer (e.g., 12): ");

        if (!sc.hasNextInt()) {
            System.out.println("Invalid input. Please enter a valid integer.");
            sc.close();
            return;
        }
        int n = sc.nextInt();

        System.out.println(describeNumber(n));
        System.out.println("Sum of digits: " + sumOfDigits(n));

        if (n >= 0 && n <= 20) {
            System.out.println("Factorial(" + n + ") = " + factorial(n));
        } else {
            System.out.println("Factorial skipped (supported here for 0..20 to keep output reasonable)." );
        }

        System.out.println("Prime? " + (isPrime(n) ? "Yes" : "No"));

        System.out.println("\nFirst 10 multiples (for-loop):");
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
        }
        sc.close();
    }
}
