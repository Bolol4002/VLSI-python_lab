/*
Experiment 06: Constructors in Java
Objective:
- Analyze how constructors work, compare different types, and implement them.

Run:
    javac Exp06Constructors.java
    java Exp06Constructors
*/

public class Exp06Constructors {
    static class Employee {
        int empId;
        String name;
        String department;

        Employee() {
            this(0, "Unknown", "General");
        }

        Employee(int empId, String name, String department) {
            this.empId = empId;
            this.name = name;
            this.department = department;
        }

        @Override
        public String toString() {
            return "Employee(id=" + empId + ", name=" + name + ", dept=" + department + ")";
        }
    }

    static class Circle {
        double radius;

        Circle(double radius) {
            this.radius = radius;
        }

        static Circle fromDiameter(double diameter) {
            return new Circle(diameter / 2);
        }

        double area() {
            double pi = 3.141592653589793;
            return pi * radius * radius;
        }
    }

    public static void main(String[] args) {
        System.out.println("Experiment 06: Constructors");

        Employee e1 = new Employee();
        Employee e2 = new Employee(101, "Alice", "R&D");
        System.out.println("Default constructor: " + e1);
        System.out.println("Parameterized constructor: " + e2);

        Circle c1 = new Circle(5);
        Circle c2 = Circle.fromDiameter(10);
        System.out.println("\nCircle radius constructor: r=" + c1.radius + ", area=" + String.format("%.2f", c1.area()));
        System.out.println("Circle fromDiameter constructor: r=" + c2.radius + ", area=" + String.format("%.2f", c2.area()));
    }
}
