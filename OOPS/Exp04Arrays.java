/*
Experiment 04: Arrays in Java
Objective:
- Apply the concept of arrays to store, access, and manipulate collections of data.

Run:
    javac Exp04Arrays.java
    java Exp04Arrays
*/

import java.util.Arrays;
import java.util.Scanner;

public class Exp04Arrays {
    static void arrayDemo() {
        int[] nums = {10, 20, 30, 40};
        System.out.println("Initial: " + Arrays.toString(nums));

        nums[2] = 25;
        System.out.println("After nums[2] = 25: " + Arrays.toString(nums));

        int target = 30;
        int index = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                index = i;
                break;
            }
        }
        System.out.println("Search 30 -> index: " + index);

        Arrays.sort(nums);
        System.out.println("After sort: " + Arrays.toString(nums));
    }

    static void matrixDemo() {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        System.out.println("\nMatrix:");
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }

    public static void main(String[] args) {
        System.out.println("Experiment 04: Arrays in Java");
        arrayDemo();
        matrixDemo();

        Scanner sc = new Scanner(System.in);
        System.out.print("\nEnter size of new array: ");
        if (!sc.hasNextInt()) {
            System.out.println("Invalid input.");
            sc.close();
            return;
        }
        int size = sc.nextInt();
        if (size < 0) {
            System.out.println("Size must be >= 0.");
            sc.close();
            return;
        }

        int[] userArr = new int[size];
        for (int i = 0; i < size; i++) {
            System.out.print("Enter element " + (i + 1) + ": ");
            if (!sc.hasNextInt()) {
                System.out.println("Invalid input.");
                sc.close();
                return;
            }
            userArr[i] = sc.nextInt();
        }
        System.out.println("Your array: " + Arrays.toString(userArr));
        sc.close();
    }
}
