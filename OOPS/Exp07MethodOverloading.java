/*
Experiment 07: Method Overloading in Java
Objective:
- Analyze the use of method overloading, differentiate it from other forms of polymorphism,
  and implement overloaded methods based on problem requirements.

Run:
    javac Exp07MethodOverloading.java
    java Exp07MethodOverloading
*/

public class Exp07MethodOverloading {
    static class Calculator {
        int add(int a, int b) {
            return a + b;
        }

        int add(int a, int b, int c) {
            return a + b + c;
        }

        double add(double a, double b) {
            return a + b;
        }
    }

    static class Printer {
        void show(int value) {
            System.out.println("int: " + value);
        }

        void show(double value) {
            System.out.println("double: " + String.format("%.2f", value));
        }

        void show(String value) {
            System.out.println("string: " + value);
        }
    }

    public static void main(String[] args) {
        System.out.println("Experiment 07: Method Overloading in Java");

        Calculator calc = new Calculator();
        System.out.println("\nCalculator.add() examples:");
        System.out.println("add(2, 3) = " + calc.add(2, 3));
        System.out.println("add(1, 2, 3) = " + calc.add(1, 2, 3));
        System.out.println("add(2.5, 3.1) = " + calc.add(2.5, 3.1));

        Printer printer = new Printer();
        System.out.println("\nPrinter.show() examples:");
        printer.show(10);
        printer.show(3.14159);
        printer.show("hello");
    }
}
