/*
Experiment 05: Classes, Objects, and Methods
Objective:
- Define custom data types, create objects, and call methods.

Run:
    javac Exp05ClassesObjectsMethods.java
    java Exp05ClassesObjectsMethods
*/

public class Exp05ClassesObjectsMethods {
    static class Student {
        int rollNo;
        String name;
        double marks;

        Student(int rollNo, String name, double marks) {
            this.rollNo = rollNo;
            this.name = name;
            this.marks = marks;
        }

        String grade() {
            if (marks >= 90) return "A";
            if (marks >= 75) return "B";
            if (marks >= 60) return "C";
            return "D";
        }

        @Override
        public String toString() {
            return "Student(rollNo=" + rollNo + ", name=" + name + ", marks=" + marks + ")";
        }
    }

    static class BankAccount {
        String holder;
        double balance;

        BankAccount(String holder, double balance) {
            this.holder = holder;
            this.balance = balance;
        }

        void deposit(double amount) {
            if (amount <= 0) throw new IllegalArgumentException("deposit amount must be positive");
            balance += amount;
        }

        void withdraw(double amount) {
            if (amount <= 0) throw new IllegalArgumentException("withdraw amount must be positive");
            if (amount > balance) throw new IllegalArgumentException("insufficient funds");
            balance -= amount;
        }

        @Override
        public String toString() {
            return "BankAccount(holder=" + holder + ", balance=" + String.format("%.2f", balance) + ")";
        }
    }

    static class Rectangle {
        double width;
        double height;

        Rectangle(double width, double height) {
            this.width = width;
            this.height = height;
        }

        double area() {
            return width * height;
        }

        double perimeter() {
            return 2 * (width + height);
        }
    }

    public static void main(String[] args) {
        System.out.println("Experiment 05: Classes, Objects, and Methods");

        Student student = new Student(101, "Alice", 84.5);
        System.out.println("Student: " + student);
        System.out.println("Grade: " + student.grade());

        BankAccount account = new BankAccount("Bob", 500);
        System.out.println("\nInitial: " + account);
        account.deposit(250);
        System.out.println("After deposit: " + account);
        account.withdraw(100);
        System.out.println("After withdraw: " + account);

        Rectangle rect = new Rectangle(4, 3);
        System.out.println("\nRectangle area: " + rect.area());
        System.out.println("Rectangle perimeter: " + rect.perimeter());
    }
}
