/*
Experiment 02: Loops to Generate Sequences
Objective:
- Implement loops to generate sequences.

Run:
    javac Exp02Sequences.java
    java Exp02Sequences
*/

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exp02Sequences {
    static List<Integer> fibonacci(int nTerms) {
        if (nTerms < 0) {
            throw new IllegalArgumentException("nTerms must be >= 0");
        }
        List<Integer> seq = new ArrayList<>();
        int a = 0, b = 1;
        for (int i = 0; i < nTerms; i++) {
            seq.add(a);
            int next = a + b;
            a = b;
            b = next;
        }
        return seq;
    }

    static List<Integer> arithmeticProgression(int a1, int d, int nTerms) {
        if (nTerms < 0) {
            throw new IllegalArgumentException("nTerms must be >= 0");
        }
        List<Integer> seq = new ArrayList<>();
        for (int i = 0; i < nTerms; i++) {
            seq.add(a1 + i * d);
        }
        return seq;
    }

    static List<Integer> geometricProgression(int a1, int r, int nTerms) {
        if (nTerms < 0) {
            throw new IllegalArgumentException("nTerms must be >= 0");
        }
        List<Integer> seq = new ArrayList<>();
        int term = a1;
        for (int i = 0; i < nTerms; i++) {
            seq.add(term);
            term *= r;
        }
        return seq;
    }

    public static void main(String[] args) {
        System.out.println("Experiment 02: Sequences using Loops");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of terms (e.g., 10): ");

        if (!sc.hasNextInt()) {
            System.out.println("Invalid input. Please enter a non-negative integer.");
            sc.close();
            return;
        }
        int n = sc.nextInt();
        if (n < 0) {
            System.out.println("Invalid input. Please enter a non-negative integer.");
            sc.close();
            return;
        }

        System.out.println("\nFibonacci (" + n + " terms): " + fibonacci(n));

        System.out.println("\nArithmetic Progression (AP):");
        System.out.print("  First term a1 (e.g., 2): ");
        if (!sc.hasNextInt()) {
            System.out.println("Invalid AP inputs.");
            sc.close();
            return;
        }
        int a1 = sc.nextInt();
        System.out.print("  Common difference d (e.g., 3): ");
        if (!sc.hasNextInt()) {
            System.out.println("Invalid AP inputs.");
            sc.close();
            return;
        }
        int d = sc.nextInt();
        System.out.println("  AP: " + arithmeticProgression(a1, d, n));

        System.out.println("\nGeometric Progression (GP):");
        System.out.print("  First term a1 (e.g., 2): ");
        if (!sc.hasNextInt()) {
            System.out.println("Invalid GP inputs.");
            sc.close();
            return;
        }
        int g1 = sc.nextInt();
        System.out.print("  Common ratio r (e.g., 2): ");
        if (!sc.hasNextInt()) {
            System.out.println("Invalid GP inputs.");
            sc.close();
            return;
        }
        int r = sc.nextInt();
        System.out.println("  GP: " + geometricProgression(g1, r, n));

        sc.close();
    }
}
