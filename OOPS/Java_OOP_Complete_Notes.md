# Java Object-Oriented Programming Complete Notes

This comprehensive guide covers all Java OOP topics from your syllabus with theory and practical code examples.

---

# Table of Contents

1. [Introduction to Object-Oriented Programming](#1-introduction-to-object-oriented-programming)
2. [OOP Principles](#2-oop-principles)
3. [Java as an Object-Oriented Language](#3-java-as-an-object-oriented-language)
4. [Data Types, Variables, and Operators](#4-data-types-variables-and-operators)
5. [Control Statements](#5-control-statements)
6. [Type Conversion and Casting](#6-type-conversion-and-casting)
7. [Classes and Objects](#7-classes-and-objects)
8. [Methods](#8-methods)
9. [Constructors](#9-constructors)
10. [Access Control and Encapsulation](#10-access-control-and-encapsulation)
11. [static and final Keywords](#11-static-and-final-keywords)
12. [Method Overloading](#12-method-overloading)
13. [Parameter Passing and Recursion](#13-parameter-passing-and-recursion)
14. [Nested Classes](#14-nested-classes)
15. [Inheritance](#15-inheritance)
16. [Method Overriding](#16-method-overriding)
17. [Abstract Classes](#17-abstract-classes)
18. [Polymorphism and Dynamic Method Dispatch](#18-polymorphism-and-dynamic-method-dispatch)
19. [Packages](#19-packages)
20. [Interfaces](#20-interfaces)
21. [Exception Handling](#21-exception-handling)
22. [String Handling](#22-string-handling)
23. [Multithreaded Programming](#23-multithreaded-programming)
24. [Java Input/Output](#24-java-inputoutput)
25. [Collection Framework](#25-collection-framework)

---

# 1. Introduction to Object-Oriented Programming

## 1.1 What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **objects** rather than functions and logic. An object is a data field that has unique attributes and behavior.

### Key Characteristics of OOP:
- **Abraction**: Hiding complex implementation details and showing only necessary features
- **Encapsulation**: Bundling data and methods that operate on that data within a single unit
- **Inheritance**: Mechanism where one class acquires the properties of another class
- **Polymorphism**: Ability to take multiple forms

## 1.2 History of OOP

- **1967**: Simula introduced class concepts
- **1972**: Smalltalk introduced message passing
- **1980s**: C++ brought OOP to mainstream
- **1995**: Java revolutionized OOP with pure object-oriented design

---

# 2. OOP Principles

## 2.1 Encapsulation

**Encapsulation** is the bundling of data (variables) and methods (functions) into a single unit (class). It also restricts direct access to some components, which is a means of preventing accidental interference and misuse of data.

### Theory:
- **Data Hiding**: Private variables with public getter/setter methods
- **Information Protection**: Prevents external code from modifying internal state directly
- **Code Maintenance**: Easier to change implementation without affecting other code

### Example Code:
```java
// Encapsulation Example - Bank Account
class BankAccount {
    // Private data members (data hiding)
    private String accountHolderName;
    private double balance;
    private String accountNumber;
    
    // Constructor
    public BankAccount(String name, String accNum, double initialBalance) {
        accountHolderName = name;
        accountNumber = accNum;
        // Validation: don't allow negative balance
        if (initialBalance >= 0) {
            balance = initialBalance;
        } else {
            balance = 0;
        }
    }
    
    // Public getter methods
    public String getAccountHolderName() {
        return accountHolderName;
    }
    
    public double getBalance() {
        return balance;
    }
    
    public String getAccountNumber() {
        return accountNumber;
    }
    
    // Public setter methods with validation
    public void setAccountHolderName(String name) {
        accountHolderName = name;
    }
    
    // Method to deposit money
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount);
            System.out.println("New Balance: " + balance);
        } else {
            System.out.println("Invalid deposit amount!");
        }
    }
    
    // Method to withdraw money
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
            System.out.println("Remaining Balance: " + balance);
        } else {
            System.out.println("Insufficient funds or invalid amount!");
        }
    }
}

public class EncapsulationDemo {
    public static void main(String[] args) {
        BankAccount account = new BankAccount("John Doe", "ACC123456", 5000);
        
        // Access through public methods (controlled access)
        System.out.println("Account Holder: " + account.getAccountHolderName());
        System.out.println("Account Number: " + account.getAccountNumber());
        System.out.println("Balance: " + account.getBalance());
        
        account.deposit(2000);
        account.withdraw(1500);
        
        // Direct access to balance is prevented (compile error if uncommented)
        // account.balance = 1000000;  // ERROR: balance has private access
    }
}
```

## 2.2 Inheritance

**Inheritance** is the mechanism by which one class acquires the properties (fields and methods) of another class.

### Theory:
- **Code Reusability**: Reuse fields and methods of existing class
- **IS-A Relationship**: Child class IS A type of parent class
- **Extensibility**: Add new features without modifying existing code
- **Types**: Single, Multilevel, Hierarchical, Multiple (through interfaces)

### Example Code:
```java
// Inheritance Example - Animal Hierarchy
class Animal {
    protected String name;
    protected int age;
    
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void eat() {
        System.out.println(name + " is eating");
    }
    
    public void sleep() {
        System.out.println(name + " is sleeping");
    }
    
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Dog inherits from Animal
class Dog extends Animal {
    private String breed;
    
    public Dog(String name, int age, String breed) {
        super(name, age);  // Call parent constructor
        this.breed = breed;
    }
    
    // Override parent's displayInfo method
    @Override
    public void displayInfo() {
        super.displayInfo();  // Call parent's displayInfo
        System.out.println("Breed: " + breed);
    }
    
    // Specific method for Dog
    public void bark() {
        System.out.println(name + " is barking: Woof! Woof!");
    }
}

// Cat inherits from Animal
class Cat extends Animal {
    private String color;
    
    public Cat(String name, int age, String color) {
        super(name, age);
        this.color = color;
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Color: " + color);
    }
    
    // Specific method for Cat
    public void meow() {
        System.out.println(name + " says: Meow!");
    }
}

public class InheritanceDemo {
    public static void main(String[] args) {
        Dog dog = new Dog("Buddy", 3, "Golden Retriever");
        Cat cat = new Cat("Whiskers", 2, "Orange");
        
        System.out.println("=== Dog Object ===");
        dog.displayInfo();
        dog.eat();
        dog.sleep();
        dog.bark();
        
        System.out.println("\n=== Cat Object ===");
        cat.displayInfo();
        cat.eat();
        cat.sleep();
        cat.meow();
    }
}
```

## 2.3 Polymorphism

**Polymorphism** allows one interface to be used for a general class of actions. The specific action is determined by the exact nature of the situation.

### Theory:
- **Compile-time Polymorphism (Static)**: Method overloading
- **Runtime Polymorphism (Dynamic)**: Method overriding
- **Upcasting**: Reference of parent type pointing to child object
- **Virtual Method Invocation**: At runtime, based on actual object type

### Example Code:
```java
// Polymorphism Example - Shape Drawing
class Shape {
    public void draw() {
        System.out.println("Drawing a shape");
    }
    
    public void calculateArea() {
        System.out.println("Calculating area");
    }
}

class Circle extends Shape {
    private double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a Circle");
    }
    
    @Override
    public void calculateArea() {
        double area = Math.PI * radius * radius;
        System.out.println("Circle Area: " + area);
    }
}

class Rectangle extends Shape {
    private double width;
    private double height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a Rectangle");
    }
    
    @Override
    public void calculateArea() {
        double area = width * height;
        System.out.println("Rectangle Area: " + area);
    }
}

class Triangle extends Shape {
    private double base;
    private double height;
    
    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a Triangle");
    }
    
    @Override
    public void calculateArea() {
        double area = 0.5 * base * height;
        System.out.println("Triangle Area: " + area);
    }
}

public class PolymorphismDemo {
    public static void main(String[] args) {
        // Array of parent type holding child objects (upcasting)
        Shape[] shapes = new Shape[4];
        shapes[0] = new Circle(5);
        shapes[1] = new Rectangle(4, 6);
        shapes[2] = new Triangle(3, 4);
        shapes[3] = new Shape();
        
        // Dynamic method dispatch at runtime
        System.out.println("=== Polymorphic Behavior ===");
        for (int i = 0; i < shapes.length; i++) {
            shapes[i].draw();
            shapes[i].calculateArea();
            System.out.println();
        }
    }
}
```

---

# 3. Java as an Object-Oriented Language

## 3.1 Java Features

### Pure Object-Oriented:
- Every piece of code is part of a class
- No standalone functions (everything belongs to some class)
- Primitive types are wrapper classes available

### Platform Independent:
- **Write Once, Run Anywhere**: Java code compiles to bytecode
- **JVM (Java Virtual Machine)**: Interprets bytecode for specific OS
- **Bytecode**: Platform-neutral intermediate code

### Key Features:
- **Simple**: No pointers, automatic memory management
- **Robust**: Exception handling, type checking
- **Multithreaded**: Built-in support for concurrent programming
- **Distributed**: Designed for network computing
- **Secure**: No direct memory access

## 3.2 Java Bytecode

Java source code (.java file) is compiled by the Java compiler (javac) into **bytecode** (.class file). This bytecode can run on any machine that has a JVM.

### Process:
1. **Source Code**: Write .java file
2. **Compilation**: `javac MyClass.java` → MyClass.class (bytecode)
3. **Interpretation**: JVM reads bytecode and executes

### Example:
```java
// HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

/*
Commands to compile and run:
---------------------------
javac HelloWorld.java
java HelloWorld

Output:
-------
Hello, World!
*/
```

## 3.3 Internet Enabled Language

Java was designed for network computing:

- **Applet**: Small Java programs that run in web browsers
- **Servlet**: Server-side Java programs
- **RMI (Remote Method Invocation)**: Distributed computing
- **Java EE**: Enterprise applications for web services
- **JSP**: Server-side scripting

---

# 4. Data Types, Variables, and Operators

## 4.1 Data Types

### Primitive Data Types (8 types):

| Type | Size | Default | Range |
|------|------|---------|-------|
| byte | 8-bit | 0 | -128 to 127 |
| short | 16-bit | 0 | -32,768 to 32,767 |
| int | 32-bit | 0 | -2³¹ to 2³¹-1 |
| long | 64-bit | 0L | -2⁶³ to 2⁶³-1 |
| float | 32-bit | 0.0f | ±3.4e38 |
| double | 64-bit | 0.0d | ±1.7e308 |
| char | 16-bit | '\u0000' | 0 to 65,535 |
| boolean | 1-bit | false | true/false |

### Reference Data Types:
- **Class types**: Objects
- **Interface types**: Interfaces
- **Array types**: Arrays

### Example Code:
```java
public class DataTypesDemo {
    public static void main(String[] args) {
        // Integer types
        byte smallNumber = 100;
        short shortNumber = 30000;
        int normalNumber = 1000000;
        long largeNumber = 10000000000L;
        
        // Floating point types
        float normalFloat = 3.14f;
        double largeDouble = 3.14159265358979;
        
        // Character type
        char grade = 'A';
        char symbol = '#';
        
        // Boolean type
        boolean isStudent = true;
        boolean hasLicense = false;
        
        // String (reference type)
        String message = "Hello Java";
        
        // Print all
        System.out.println("byte: " + smallNumber);
        System.out.println("short: " + shortNumber);
        System.out.println("int: " + normalNumber);
        System.out.println("long: " + largeNumber);
        System.out.println("float: " + normalFloat);
        System.out.println("double: " + largeDouble);
        System.out.println("char: " + grade);
        System.out.println("boolean: " + isStudent);
        System.out.println("String: " + message);
        
        // Find size of each type
        System.out.println("\n=== Size of Data Types ===");
        System.out.println("byte size: " + Byte.SIZE + " bits");
        System.out.println("short size: " + Short.SIZE + " bits");
        System.out.println("int size: " + Integer.SIZE + " bits");
        System.out.println("long size: " + Long.SIZE + " bits");
        System.out.println("float size: " + Float.SIZE + " bits");
        System.out.println("double size: " + Double.SIZE + " bits");
        System.out.println("char size: " + Character.SIZE + " bits");
    }
}
```

## 4.2 Variables

### Variable Declaration and Initialization:
```java
public class VariablesDemo {
    // Instance variables (non-static)
    String name = "John";
    int age = 25;
    
    // Static variables (class variables)
    static String company = "TechCorp";
    
    public static void main(String[] args) {
        // Local variables
        int localVar = 10;
        
        // Dynamic initialization
        int a = 5, b = 10;
        int sum = a + b;  // Dynamic initialization
        
        System.out.println("Local Variable: " + localVar);
        System.out.println("Sum: " + sum);
        
        // Creating object to access instance variables
        VariablesDemo obj = new VariablesDemo();
        System.out.println("Instance Variable - Name: " + obj.name);
        System.out.println("Static Variable - Company: " + company);
    }
}
```

### Scope and Lifetime:

| Variable Type | Scope | Lifetime |
|--------------|-------|----------|
| Instance | Throughout class | Object lifetime |
| Static | Throughout class | Program lifetime |
| Local | Within method | Method execution |
| Block | Within block {} | Block execution |

### Example Code:
```java
public class ScopeLifetimeDemo {
    // Instance variable
    int instanceVar = 10;
    
    // Static variable
    static int staticVar = 20;
    
    public void method() {
        // Local variable
        int localVar = 30;
        
        System.out.println("Instance: " + instanceVar);
        System.out.println("Static: " + staticVar);
        System.out.println("Local: " + localVar);
        
        // Block variable
        {
            int blockVar = 40;
            System.out.println("Block: " + blockVar);
        }
        // blockVar is not accessible here
    }
    
    public static void main(String[] args) {
        ScopeLifetimeDemo obj = new ScopeLifetimeDemo();
        obj.method();
    }
}
```

## 4.3 Operators

### Arithmetic Operators:
```java
public class OperatorsDemo {
    public static void main(String[] args) {
        int a = 10, b = 3;
        
        // Arithmetic operators
        System.out.println("a + b = " + (a + b));  // 13
        System.out.println("a - b = " + (a - b));  // 7
        System.out.println("a * b = " + (a * b));  // 30
        System.out.println("a / b = " + (a / b));  // 3 (integer division)
        System.out.println("a % b = " + (a % b));  // 1
        
        // Increment/Decrement
        int c = 5;
        System.out.println("\n++c = " + (++c));  // 6 (pre-increment)
        System.out.println("c++ = " + (c++));  // 6, then c=7
        
        // Assignment operators
        int d = 10;
        d += 5;  // d = d + 5 = 15
        d -= 3;  // d = d - 3 = 12
        d *= 2;  // d = d * 2 = 24
        d /= 4;  // d = d / 4 = 6
        d %= 5;  // d = d % 5 = 1
        
        // Comparison operators
        System.out.println("\n10 == 5: " + (10 == 5));   // false
        System.out.println("10 != 5: " + (10 != 5));   // true
        System.out.println("10 > 5: " + (10 > 5));    // true
        System.out.println("10 < 5: " + (10 < 5));    // false
        System.out.println("10 >= 5: " + (10 >= 5));  // true
        
        // Logical operators
        boolean x = true, y = false;
        System.out.println("\nx && y: " + (x && y));  // false
        System.out.println("x || y: " + (x || y));  // true
        System.out.println("!x: " + (!x));          // false
        
        // Bitwise operators
        int p = 5, q = 3;  // 5=101, 3=011
        System.out.println("\np & q = " + (p & q));  // 1 (001)
        System.out.println("p | q = " + (p | q));  // 7 (111)
        System.out.println("p ^ q = " + (p ^ q));  // 6 (110)
        System.out.println("~p = " + (~p));       // -6
        
        // Shift operators
        int r = 8;  // 1000
        System.out.println("\nr << 2 = " + (r << 2));  // 32 (100000)
        System.out.println("r >> 2 = " + (r >> 2));  // 2 (10)
    }
}
```

---

# 5. Control Statements

## 5.1 Decision Making Statements

### if-else Statement:
```java
public class IfElseDemo {
    public static void main(String[] args) {
        int age = 20;
        
        // Simple if
        if (age >= 18) {
            System.out.println("Eligible to vote");
        }
        
        // if-else
        if (age >= 18) {
            System.out.println("Adult");
        } else {
            System.out.println("Minor");
        }
        
        // if-else-if ladder
        int marks = 75;
        
        if (marks >= 90) {
            System.out.println("Grade: A+");
        } else if (marks >= 80) {
            System.out.println("Grade: A");
        } else if (marks >= 70) {
            System.out.println("Grade: B+");
        } else if (marks >= 60) {
            System.out.println("Grade: B");
        } else if (marks >= 50) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: F");
        }
        
        // Nested if
        int num = 10;
        if (num > 0) {
            if (num % 2 == 0) {
                System.out.println("Positive even number");
            } else {
                System.out.println("Positive odd number");
            }
        } else {
            System.out.println("Negative number");
        }
    }
}
```

### switch Statement:
```java
public class SwitchDemo {
    public static void main(String[] args) {
        int day = 3;
        String dayName;
        
        // switch with int
        switch (day) {
            case 1:
                dayName = "Sunday";
                break;
            case 2:
                dayName = "Monday";
                break;
            case 3:
                dayName = "Tuesday";
                break;
            case 4:
                dayName = "Wednesday";
                break;
            case 5:
                dayName = "Thursday";
                break;
            case 6:
                dayName = "Friday";
                break;
            case 7:
                dayName = "Saturday";
                break;
            default:
                dayName = "Invalid day";
        }
        System.out.println("Day: " + dayName);
        
        // switch with String (Java 7+)
        String grade = "A";
        switch (grade) {
            case "A+":
            case "A":
                System.out.println("Excellent");
                break;
            case "B":
                System.out.println("Good");
                break;
            case "C":
                System.out.println("Average");
                break;
            default:
                System.out.println("Needs Improvement");
        }
        
        // switch expression (Java 14+)
        int num = 2;
        String result = switch (num) {
            case 1 -> "One";
            case 2 -> "Two";
            case 3 -> "Three";
            default -> "Other";
        };
        System.out.println("Number: " + result);
    }
}
```

## 5.2 Loop Statements

### for Loop:
```java
public class ForLoopDemo {
    public static void main(String[] args) {
        // Basic for loop
        System.out.println("=== Basic For Loop ===");
        for (int i = 1; i <= 5; i++) {
            System.out.println("Count: " + i);
        }
        
        // Enhanced for loop (for-each)
        System.out.println("\n=== Enhanced For Loop ===");
        String[] fruits = {"Apple", "Banana", "Orange", "Mango"};
        for (String fruit : fruits) {
            System.out.println("Fruit: " + fruit);
        }
        
        // Nested for loop
        System.out.println("\n=== Multiplication Table ===");
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= 5; j++) {
                System.out.print(i * j + "\t");
            }
            System.out.println();
        }
    }
}
```

### while Loop:
```java
public class WhileLoopDemo {
    public static void main(String[] args) {
        // while loop
        System.out.println("=== While Loop ===");
        int count = 1;
        while (count <= 5) {
            System.out.println("Count: " + count);
            count++;
        }
        
        // do-while loop (executes at least once)
        System.out.println("\n=== Do-While Loop ===");
        int num = 1;
        do {
            System.out.println("Number: " + num);
            num++;
        } while (num <= 5);
        
        // Find sum of digits
        System.out.println("\n=== Sum of Digits ===");
        int number = 12345;
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        System.out.println("Sum of digits: " + sum);
    }
}
```

## 5.3 Jump Statements

### break, continue, return:
```java
public class JumpDemo {
    public static void main(String[] args) {
        // break - exits loop
        System.out.println("=== Break Example ===");
        for (int i = 1; i <= 10; i++) {
            if (i == 5) {
                System.out.println("Breaking at i = " + i);
                break;
            }
            System.out.println("i = " + i);
        }
        
        // continue - skips iteration
        System.out.println("\n=== Continue Example ===");
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                continue;  // Skip this iteration
            }
            System.out.println("i = " + i);
        }
        
        // labelled break and continue
        System.out.println("\n=== Labelled Break ===");
        outer:
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    break outer;
                }
                System.out.println("i=" + i + ", j=" + j);
            }
        }
    }
}
```

---

# 6. Type Conversion and Casting

## 6.1 Type Conversion

### Widening (Automatic) Conversion:
- byte → short → int → long → float → double
- char → int → long → float → double

```java
public class TypeConversion {
    public static void main(String[] args) {
        // Automatic (widening) conversion
        int intVal = 100;
        long longVal = intVal;  // int to long (automatic)
        float floatVal = longVal;  // long to float (automatic)
        double doubleVal = floatVal;  // float to double (automatic)
        
        System.out.println("Int: " + intVal);
        System.out.println("Long: " + longVal);
        System.out.println("Float: " + floatVal);
        System.out.println("Double: " + doubleVal);
        
        // Character to int
        char ch = 'A';
        int charToInt = ch;  // char to int
        System.out.println("\nChar: " + ch);
        System.out.println("As int: " + charToInt);
    }
}
```

## 6.2 Casting

### Narrowing (Explicit) Conversion:
```java
public class Casting {
    public static void main(String[] args) {
        double d = 100.99;
        int i = (int) d;  // explicit cast
        System.out.println("Double: " + d);
        System.out.println("After cast to int: " + i);
        
        // More examples
        long l = 1000;
        byte b = (byte) l;  // long to byte
        System.out.println("\nLong: " + l);
        System.out.println("As byte: " + b);
        
        // Truncation behavior
        double pi = 3.14159;
        int truncated = (int) pi;
        System.out.println("\nPI: " + pi);
        System.out.println("Truncated: " + truncated);
        
        // Overflow example
        byte overflow = (byte) 130;  // exceeds byte range
        System.out.println("\n130 as byte: " + overflow);
    }
}
```

### Example with Arithmetic:
```java
public class ArithmeticCasting {
    public static void main(String[] args) {
        int a = 10, b = 3;
        double division = (double) a / b;  // cast for decimal result
        System.out.println("Integer division: " + (a / b));
        System.out.println("With casting: " + division);
        
        // Type promotion in expressions
        int x = 10;
        double y = 20.5;
        // int z = x + y;  // Error: can't assign double to int
        double z = x + y;  // OK: int promoted to double
        System.out.println("\nx + y = " + z);
    }
}
```

---

# 7. Classes and Objects

## 7.1 Class Definition

A class is a blueprint for creating objects. It defines:
- **Fields (attributes)**: Data variables
- **Methods (behaviors)**: Functions operating on data
- **Constructors**: Special methods to initialize objects

```java
// Class definition
class Student {
    // Data members (fields/instance variables)
    private String name;
    private int age;
    private String studentId;
    private double GPA;
    
    // Constructor (to initialize object)
    public Student(String name, int age, String id) {
        this.name = name;
        this.age = age;
        this.studentId = id;
        this.GPA = 0.0;
    }
    
    // Getter methods
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public String getStudentId() {
        return studentId;
    }
    
    public double getGPA() {
        return GPA;
    }
    
    // Setter methods
    public void setName(String name) {
        this.name = name;
    }
    
    public void setGPA(double GPA) {
        if (GPA >= 0.0 && GPA <= 4.0) {
            this.GPA = GPA;
        }
    }
    
    // Other methods
    public void displayInfo() {
        System.out.println("Student ID: " + studentId);
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("GPA: " + GPA);
    }
}
```

## 7.2 Creating Objects

```java
public class ClassObjectDemo {
    public static void main(String[] args) {
        // Creating objects using constructor
        Student student1 = new Student("John Doe", 20, "S001");
        Student student2 = new Student("Jane Smith", 21, "S002");
        
        // Using object methods
        student1.setGPA(3.8);
        student2.setGPA(3.9);
        
        System.out.println("=== Student 1 ===");
        student1.displayInfo();
        
        System.out.println("\n=== Student 2 ===");
        student2.displayInfo();
        
        // Assigning reference variables
        Student student3 = student1;
        System.out.println("\n=== Student 3 (same as student1) ===");
        student3.displayInfo();
        
        // Checking object equality
        System.out.println("\nstudent1 == student3: " + (student1 == student3));
        System.out.println("student1 == student2: " + (student1 == student2));
    }
}
```

## 7.3 Declaring and Assigning Objects

```java
public class ObjectReferenceDemo {
    public static void main(String[] args) {
        // Declare object reference
        Student studentRef;
        
        // Create new object and assign to reference
        studentRef = new Student("Alice", 22, "S003");
        
        // Declare and initialize in one statement
        Student studentRef2 = new Student("Bob", 21, "S004");
        
        // Assign one reference to another
        Student studentRef3 = studentRef2;
        
        // All three references point to same object
        System.out.println("studentRef: " + studentRef.getName());
        System.out.println("studentRef2: " + studentRef2.getName());
        System.out.println("studentRef3: " + studentRef3.getName());
        
        // Reassign reference
        studentRef = studentRef2;
        System.out.println("\nAfter reassignment:");
        System.out.println("studentRef: " + studentRef.getName());
    }
}
```

---

# 8. Methods

## 8.1 Method Definition and Calling

```java
public class MethodDemo {
    // Instance method
    public void displayMessage() {
        System.out.println("Hello from instance method!");
    }
    
    // Method with parameters
    public int add(int a, int b) {
        return a + b;
    }
    
    // Method with return type
    public String getFullName(String firstName, String lastName) {
        return firstName + " " + lastName;
    }
    
    // Method overloading (different parameter types)
    public int add(int a, int b, int c) {
        return a + b + c;
    }
    
    public double add(double a, double b) {
        return a + b;
    }
    
    public static void main(String[] args) {
        MethodDemo obj = new MethodDemo();
        
        // Calling methods
        obj.displayMessage();
        
        System.out.println("Sum: " + obj.add(5, 10));
        System.out.println("Full Name: " + obj.getFullName("John", "Doe"));
        
        // Method overloading resolution at compile time
        System.out.println("Sum 3 numbers: " + obj.add(1, 2, 3));
        System.out.println("Sum doubles: " + obj.add(2.5, 3.5));
    }
}
```

## 8.2 Static Methods

```java
public class StaticMethodDemo {
    // Static variable
    static int count = 0;
    
    // Instance variable
    String name;
    
    // Static method
    public static void displayCount() {
        System.out.println("Count: " + count);
    }
    
    // Static method with parameter
    public static int increment(int value) {
        count++;
        return count + value;
    }
    
    // Main method (static)
    public static void main(String[] args) {
        // Call static method directly
        displayCount();
        
        int result = increment(10);
        System.out.println("After increment: " + result);
        displayCount();
        
        // Cannot call instance method directly in static context
        // name = "Test";  // Error
        
        StaticMethodDemo obj = new StaticMethodDemo();
        obj.name = "Instance variable";
        System.out.println("Name: " + obj.name);
    }
}
```

---

# 9. Constructors

## 9.1 Constructor Types

```java
class Box {
    private double width;
    private double height;
    private double depth;
    
    // Default constructor
    public Box() {
        width = 1;
        height = 1;
        depth = 1;
    }
    
    // Parameterized constructor
    public Box(double width, double height, double depth) {
        this.width = width;
        this.height = height;
        this.depth = depth;
    }
    
    // Copy constructor
    public Box(Box box) {
        this.width = box.width;
        this.height = box.height;
        this.depth = box.depth;
    }
    
    // Calculate volume
    public double volume() {
        return width * height * depth;
    }
    
    // Display dimensions
    public void display() {
        System.out.println("Dimensions: " + width + " x " + height + " x " + depth);
    }
}

public class ConstructorDemo {
    public static void main(String[] args) {
        // Using default constructor
        Box box1 = new Box();
        System.out.println("Box 1 (default):");
        box1.display();
        System.out.println("Volume: " + box1.volume());
        
        // Using parameterized constructor
        Box box2 = new Box(5, 3, 2);
        System.out.println("\nBox 2 (parameterized):");
        box2.display();
        System.out.println("Volume: " + box2.volume());
        
        // Using copy constructor
        Box box3 = new Box(box2);
        System.out.println("\nBox 3 (copy of box2):");
        box3.display();
        System.out.println("Volume: " + box3.volume());
    }
}
```

## 9.2 Constructor Overloading

```java
class Rectangle {
    private double length;
    private double breadth;
    
    // No-argument constructor
    public Rectangle() {
        this.length = 1;
        this.breadth = 1;
    }
    
    // One-parameter constructor
    public Rectangle(double side) {
        this.length = side;
        this.breadth = side;
    }
    
    // Two-parameter constructor
    public Rectangle(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }
    
    public double area() {
        return length * breadth;
    }
    
    public void display() {
        System.out.println("Length: " + length + ", Breadth: " + breadth);
    }
}

public class ConstructorOverloadingDemo {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle();
        Rectangle r2 = new Rectangle(5);
        Rectangle r3 = new Rectangle(4, 6);
        
        System.out.println("Rectangle 1 (default):");
        r1.display();
        System.out.println("Area: " + r1.area());
        
        System.out.println("\nRectangle 2 (square):");
        r2.display();
        System.out.println("Area: " + r2.area());
        
        System.out.println("\nRectangle 3 (rectangle):");
        r3.display();
        System.out.println("Area: " + r3.area());
    }
}
```

---

# 10. Access Control and Encapsulation

## 10.1 Access Modifiers

| Modifier | Class | Package | Subclass | World |
|----------|-------|---------|----------|-------|
| public | Yes | Yes | Yes | Yes |
| protected | Yes | Yes | Yes | No |
| default | Yes | Yes | No | No |
| private | Yes | No | No | No |

```java
// Access modifiers demonstration

package mypackage;

public class AccessDemo {
    // Only accessible within the class
    private String privateVar = "Private";
    
    // Accessible within package (default)
    String defaultVar = "Default";
    
    // Accessible everywhere
    public String publicVar = "Public";
    
    // Accessible within package and subclasses
    protected String protectedVar = "Protected";
    
    // Private method
    private void privateMethod() {
        System.out.println("Private method");
    }
    
    // Public method
    public void publicMethod() {
        System.out.println("Public method");
    }
    
    // Protected method
    protected void protectedMethod() {
        System.out.println("Protected method");
    }
    
    // Package-private method
    void defaultMethod() {
        System.out.println("Default method");
    }
}

public class AccessTest {
    public static void main(String[] args) {
        AccessDemo obj = new AccessDemo();
        
        // Accessible in same class
        System.out.println(obj.privateVar);
        System.out.println(obj.defaultVar);
        System.out.println(obj.publicVar);
        System.out.println(obj.protectedVar);
        
        obj.privateMethod();
        obj.publicMethod();
        obj.protectedMethod();
        obj.defaultMethod();
    }
}
```

---

# 11. static and final Keywords

## 11.1 static Keyword

```java
class StaticDemo {
    // Instance variable - each object has its own copy
    int instanceVar = 10;
    
    // Static variable - shared by all objects of the class
    static int staticVar = 20;
    
    // Instance method
    public void instanceMethod() {
        System.out.println("Instance method");
    }
    
    // Static method
    public static void staticMethod() {
        System.out.println("Static method");
    }
    
    // Static block - executed once when class is loaded
    static {
        System.out.println("Static block executed");
    }
    
    public static void main(String[] args) {
        // Accessing static variable without object
        System.out.println("Static variable: " + StaticDemo.staticVar);
        
        // Calling static method without object
        StaticDemo.staticMethod();
        
        // Creating objects
        StaticDemo obj1 = new StaticDemo();
        StaticDemo obj2 = new StaticDemo();
        
        // Modifying through object
        obj1.instanceVar = 100;
        obj2.instanceVar = 200;
        
        // Modifying static variable through object
        obj1.staticVar = 300;
        
        // Static variable is shared
        System.out.println("\nobj1.instanceVar: " + obj1.instanceVar);
        System.out.println("obj2.instanceVar: " + obj2.instanceVar);
        System.out.println("Static var (from obj1): " + obj1.staticVar);
        System.out.println("Static var (from obj2): " + obj2.staticVar);
    }
}
```

## 11.2 final Keyword

```java
class FinalDemo {
    // Final variable - constant
    final int CONSTANT_VALUE = 100;
    
    // Final static variable
    final static double PI = 3.14159;
    
    // Blank final - initialized in constructor
    final int value;
    
    // Static final variable
    static final String APP_NAME = "MyApp";
    
    // Constructor
    public FinalDemo() {
        value = 50;  // Initialize blank final
    }
    
    // Final method - cannot be overridden
    public final void display() {
        System.out.println("Value: " + value);
    }
}

// Final class - cannot be inherited
final class FinalClass {
    public void show() {
        System.out.println("Final class method");
    }
}

// Cannot extend final class
// class SubClass extends FinalClass { }  // ERROR

public class FinalKeywordDemo {
    public static void main(String[] args) {
        FinalDemo obj = new FinalDemo();
        
        System.out.println("Constant: " + obj.CONSTANT_VALUE);
        System.out.println("Value: " + obj.value);
        System.out.println("PI: " + FinalDemo.PI);
        System.out.println("App Name: " + FinalDemo.APP_NAME);
        
        // Cannot modify final variable
        // obj.CONSTANT_VALUE = 200;  // ERROR
        
        obj.display();
    }
}
```

---

# 12. Method Overloading

Methods with same name but different parameters within the same class.

```java
class Calculator {
    // Add two integers
    public int add(int a, int b) {
        return a + b;
    }
    
    // Add three integers
    public int add(int a, int b, int c) {
        return a + b + c;
    }
    
    // Add two doubles
    public double add(double a, double b) {
        return a + b;
    }
    
    // Add integer and double
    public double add(int a, double b) {
        return a + b;
    }
    
    // Add arrays
    public int add(int[] arr) {
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return sum;
    }
}

public class MethodOverloadingDemo {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        System.out.println("Add(5, 3): " + calc.add(5, 3));
        System.out.println("Add(5, 3, 2): " + calc.add(5, 3, 2));
        System.out.println("Add(5.5, 3.5): " + calc.add(5.5, 3.5));
        System.out.println("Add(5, 3.5): " + calc.add(5, 3.5));
        
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("Add array: " + calc.add(numbers));
    }
}
```

---

# 13. Parameter Passing and Recursion

## 13.1 Call by Value

```java
class ParameterPassing {
    // Pass by value - primitive types
    public void modifyPrimitive(int num) {
        num = 100;
        System.out.println("Inside method: " + num);
    }
    
    // Pass by value - reference types (copy of reference)
    public void modifyObject(StringBuilder sb) {
        sb.append(" World");
        System.out.println("Inside method: " + sb);
    }
    
    // Swap - doesn't work (pass by value)
    public void swap(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
    }
    
    // Correct swap using arrays
    public void swap(int[] arr) {
        int temp = arr[0];
        arr[0] = arr[1];
        arr[1] = temp;
    }
    
    public static void main(String[] args) {
        ParameterPassing obj = new ParameterPassing();
        
        // Primitive - original unchanged
        int num = 50;
        System.out.println("Before: " + num);
        obj.modifyPrimitive(num);
        System.out.println("After: " + num);
        
        // StringBuilder - original changed (same object)
        StringBuilder sb = new StringBuilder("Hello");
        System.out.println("\nBefore: " + sb);
        obj.modifyObject(sb);
        System.out.println("After: " + sb);
        
        // Swap demonstration
        int a = 5, b = 10;
        obj.swap(a, b);
        System.out.println("\nAfter swap (primitive): a=" + a + ", b=" + b);
        
        int[] arr = {5, 10};
        obj.swap(arr);
        System.out.println("After swap (array): arr[0]=" + arr[0] + ", arr[1]=" + arr[1]);
    }
}
```

## 13.2 Recursion

```java
class RecursionDemo {
    // Factorial using recursion
    public int factorial(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
    
    // Fibonacci using recursion
    public int fibonacci(int n) {
        if (n <= 1) {
            return n;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
    
    // Sum of array using recursion
    public int sumArray(int[] arr, int index) {
        if (index >= arr.length) {
            return 0;
        } else {
            return arr[index] + sumArray(arr, index + 1);
        }
    }
    
    // Reverse a string using recursion
    public String reverseString(String str) {
        if (str.isEmpty()) {
            return str;
        } else {
            return str.charAt(str.length() - 1) + 
                   reverseString(str.substring(0, str.length() - 1));
        }
    }
    
    // Tower of Hanoi
    public void towerOfHanoi(int n, char from, char to, char aux) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + from + " to " + to);
            return;
        }
        towerOfHanoi(n - 1, from, aux, to);
        System.out.println("Move disk " + n + " from " + from + " to " + to);
        towerOfHanoi(n - 1, aux, to, from);
    }
    
    public static void main(String[] args) {
        RecursionDemo obj = new RecursionDemo();
        
        System.out.println("Factorial of 5: " + obj.factorial(5));
        
        System.out.println("\nFibonacci series (first 10):");
        for (int i = 0; i < 10; i++) {
            System.out.print(obj.fibonacci(i) + " ");
        }
        
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println("\n\nSum of array: " + obj.sumArray(arr, 0));
        
        System.out.println("Reverse of 'Hello': " + obj.reverseString("Hello"));
        
        System.out.println("\nTower of Hanoi (3 disks):");
        obj.towerOfHanoi(3, 'A', 'C', 'B');
    }
}
```

---

# 14. Nested Classes

## 14.1 Types of Nested Classes

```java
// Outer class
class OuterClass {
    private String outerField = "Outer";
    
    // Static nested class
    static class StaticNestedClass {
        public void display() {
            System.out.println("Static nested class");
        }
    }
    
    // Non-static (inner) class
    class InnerClass {
        public void display() {
            System.out.println("Inner class - " + outerField);
        }
    }
    
    // Method-local inner class
    public void displayMethod() {
        final int localVar = 10;
        
        class MethodLocalClass {
            public void display() {
                System.out.println("Method local class - " + localVar);
            }
        }
        
        MethodLocalClass obj = new MethodLocalClass();
        obj.display();
    }
    
    // Anonymous inner class
    public Runnable getRunnable() {
        return new Runnable() {
            @Override
            public void run() {
                System.out.println("Anonymous inner class running");
            }
        };
    }
}

public class NestedClassDemo {
    public static void main(String[] args) {
        // Create static nested class (no outer object needed)
        OuterClass.StaticNestedClass staticObj = new OuterClass.StaticNestedClass();
        staticObj.display();
        
        // Create non-static inner class (requires outer object)
        OuterClass outer = new OuterClass();
        OuterClass.InnerClass inner = outer.new InnerClass();
        inner.display();
        
        // Method-local inner class
        outer.displayMethod();
        
        // Anonymous inner class
        Runnable r = outer.getRunnable();
        r.run();
        
        // Another anonymous class example
        Runnable anonymous = new Runnable() {
            @Override
            public void run() {
                System.out.println("Anonymous class 2");
            }
        };
        anonymous.run();
    }
}
```

---

# 15. Inheritance

## 15.1 Types of Inheritance

```java
// Single Inheritance
class Animal {
    protected String name;
    public Animal(String name) {
        this.name = name;
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }
    public void bark() {
        System.out.println(name + " barks");
    }
}

// Multilevel Inheritance
class Mammal extends Animal {
    public Mammal(String name) {
        super(name);
    }
}

class Cat extends Mammal {
    public Cat(String name) {
        super(name);
    }
}

// Hierarchical Inheritance
class Bird extends Animal {
    public Bird(String name) {
        super(name);
    }
    public void fly() {
        System.out.println(name + " flies");
    }
}

// Multiple inheritance through interface
interface Runner {
    void run();
}

interface Swimmer {
    void swim();
}

// Class implementing multiple interfaces
class Duck extends Animal implements Runner, Swimmer {
    public Duck(String name) {
        super(name);
    }
    
    @Override
    public void run() {
        System.out.println(name + " runs");
    }
    
    @Override
    public void swim() {
        System.out.println(name + " swims");
    }
}

public class InheritanceTypesDemo {
    public static void main(String[] args) {
        // Single inheritance
        Dog dog = new Dog("Buddy");
        System.out.println("=== Dog (Single Inheritance) ===");
        System.out.println("Name: " + dog.name);
        dog.bark();
        
        // Multilevel inheritance
        Cat cat = new Cat("Whiskers");
        System.out.println("\n=== Cat (Multilevel Inheritance) ===");
        System.out.println("Name: " + cat.name);
        cat.meow();  // inherited from Mammal if defined
        
        // Hierarchical inheritance
        Bird bird = new Bird("Tweety");
        System.out.println("\n=== Bird (Hierarchical Inheritance) ===");
        bird.fly();
        
        // Multiple inheritance through interfaces
        Duck duck = new Duck("Donald");
        System.out.println("\n=== Duck (Multiple Interfaces) ===");
        duck.run();
        duck.swim();
    }
}
```

## 15.2 Using super Keyword

```java
class Shape {
    protected String color;
    
    public Shape() {
        System.out.println("Shape constructor called");
    }
    
    public Shape(String color) {
        this.color = color;
    }
    
    public void displayColor() {
        System.out.println("Color: " + color);
    }
}

class Rectangle extends Shape {
    private int width;
    private int height;
    
    // Using super to call parent constructor
    public Rectangle() {
        super();  // calls Shape()
        System.out.println("Rectangle constructor called");
    }
    
    public Rectangle(String color, int width, int height) {
        super(color);  // calls Shape(String color)
        this.width = width;
        this.height = height;
    }
    
    // Using super to access parent method
    public void display() {
        super.displayColor();  // calls parent's method
        System.out.println("Width: " + width);
        System.out.println("Height: " + height);
    }
}

public class SuperKeywordDemo {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle("Blue", 10, 5);
        rect.display();
    }
}
```

---

# 16. Method Overriding

```java
class Vehicle {
    public void start() {
        System.out.println("Starting vehicle");
    }
    
    public void stop() {
        System.out.println("Stopping vehicle");
    }
    
    public void run() {
        System.out.println("Vehicle is running");
    }
}

class Car extends Vehicle {
    // Method overriding
    @Override
    public void start() {
        System.out.println("Starting car");
    }
    
    @Override
    public void run() {
        System.out.println("Car is driving at 60 mph");
    }
    
    // Specific method
    public void honk() {
        System.out.println("Car honking: Beep! Beep!");
    }
}

class Bike extends Vehicle {
    @Override
    public void start() {
        System.out.println("Starting bike");
    }
    
    @Override
    public void run() {
        System.out.println("Bike is moving at 30 mph");
    }
}

public class MethodOverridingDemo {
    public static void main(String[] args) {
        // Upcasting
        Vehicle vehicle1 = new Car();
        Vehicle vehicle2 = new Bike();
        
        System.out.println("=== Car (upcasted) ===");
        vehicle1.start();
        vehicle1.run();
        // vehicle1.honk();  // Not accessible
        
        System.out.println("\n=== Bike (upcasted) ===");
        vehicle2.start();
        vehicle2.run();
        
        // Downcasting
        Car car = (Car) vehicle1;
        car.honk();  // Now accessible
        
        // Using instanceof
        if (vehicle1 instanceof Car) {
            Car car2 = (Car) vehicle1;
            car2.honk();
        }
    }
}
```

---

# 17. Abstract Classes

```java
// Abstract class
abstract class Shape {
    protected String color;
    
    // Constructor
    public Shape(String color) {
        this.color = color;
    }
    
    // Abstract method - no implementation
    public abstract double getArea();
    
    public abstract double getPerimeter();
    
    // Concrete method
    public void displayColor() {
        System.out.println("Color: " + color);
    }
}

// Concrete implementation
class Circle extends Shape {
    private double radius;
    
    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }
}

class Rectangle extends Shape {
    private double width;
    private double height;
    
    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }
    
    @Override
    public double getArea() {
        return width * height;
    }
    
    @Override
    public double getPerimeter() {
        return 2 * (width + height);
    }
}

public class AbstractClassDemo {
    public static void main(String[] args) {
        // Cannot create instance of abstract class
        // Shape shape = new Shape("Red");  // ERROR
        
        // Create instances of concrete classes
        Circle circle = new Circle("Red", 5);
        Rectangle rectangle = new Rectangle("Blue", 4, 3);
        
        System.out.println("=== Circle ===");
        circle.displayColor();
        System.out.println("Area: " + circle.getArea());
        System.out.println("Perimeter: " + circle.getPerimeter());
        
        System.out.println("\n=== Rectangle ===");
        rectangle.displayColor();
        System.out.println("Area: " + rectangle.getArea());
        System.out.println("Perimeter: " + rectangle.getPerimeter());
        
        // Polymorphic behavior
        Shape[] shapes = {circle, rectangle};
        for (Shape s : shapes) {
            System.out.println("\n=== Shape ===");
            s.displayColor();
            System.out.println("Area: " + s.getArea());
        }
    }
}
```

---

# 18. Polymorphism and Dynamic Method Dispatch

```java
class Bank {
    public double calculateInterest(double principal, double rate) {
        return principal * rate;
    }
}

class SBI extends Bank {
    @Override
    public double calculateInterest(double principal, double rate) {
        System.out.println("SBI Bank Interest");
        return principal * rate * 1.1;  // 10% extra
    }
}

class HDFC extends Bank {
    @Override
    public double calculateInterest(double principal, double rate) {
        System.out.println("HDFC Bank Interest");
        return principal * rate * 1.2;  // 20% extra
    }
}

class ICICI extends Bank {
    @Override
    public double calculateInterest(double principal, double rate) {
        System.out.println("ICICI Bank Interest");
        return principal * rate * 1.15;  // 15% extra
    }
}

public class PolymorphismDemo {
    public static void main(String[] args) {
        Bank bank;
        
        // Dynamic method dispatch
        bank = new SBI();
        System.out.println("SBI Interest: " + bank.calculateInterest(1000, 0.1));
        
        bank = new HDFC();
        System.out.println("HDFC Interest: " + bank.calculateInterest(1000, 0.1));
        
        bank = new ICICI();
        System.out.println("ICICI Interest: " + bank.calculateInterest(1000, 0.1));
        
        // Polymorphic array
        Bank[] banks = {new SBI(), new HDFC(), new ICICI()};
        double totalInterest = 0;
        for (Bank b : banks) {
            totalInterest += b.calculateInterest(1000, 0.1);
        }
        System.out.println("\nTotal Interest: " + totalInterest);
    }
}
```

---

# 19. Packages

## 19.1 Creating and Using Packages

```java
// Package is a folder containing related classes
// File 1: utility/myutil/MathUtils.java
package myutil;

public class MathUtils {
    public static int add(int a, int b) {
        return a + b;
    }
    
    public static int subtract(int a, int b) {
        return a - b;
    }
    
    public static int multiply(int a, int b) {
        return a * b;
    }
    
    public static double divide(int a, int b) {
        if (b != 0) {
            return (double) a / b;
        }
        return 0;
    }
}

// File 2: model/Student.java
package model;

public class Student {
    private String name;
    private int age;
    
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Main class
import myutil.MathUtils;
import model.Student;

public class PackageDemo {
    public static void main(String[] args) {
        // Using MathUtils from myutil package
        System.out.println("Add: " + MathUtils.add(10, 5));
        System.out.println("Subtract: " + MathUtils.subtract(10, 5));
        System.out.println("Multiply: " + MathUtils.multiply(10, 5));
        System.out.println("Divide: " + MathUtils.divide(10, 5));
        
        // Using Student from model package
        Student student = new Student("John", 20);
        student.display();
    }
}
```

## 19.2 Classpath

```bash
# Compile with classpath
javac -d . *.java

# Compile with external classpath
javac -cp "/path/to/external.jar" MyClass.java

# Run with classpath
java -cp . PackageDemo

# Set classpath environment
export CLASSPATH=/path/to/lib
```

---

# 20. Interfaces

## 20.1 Interface Declaration and Implementation

```java
// Interface definition
interface Drawable {
    // Abstract method (public abstract by default)
    void draw();
    
    // Default method (Java 8+)
    default void display() {
        System.out.println("Displaying drawable");
    }
    
    // Static method (Java 8+)
    static void printMessage() {
        System.out.println("Static method in interface");
    }
}

// Another interface
interface Movable {
    void move();
}

// Concrete class implementing interface
class Circle implements Drawable {
    private double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing Circle with radius " + radius);
    }
}

// Multiple interfaces
class Animal implements Movable, Drawable {
    private String name;
    
    public Animal(String name) {
        this.name = name;
    }
    
    @Override
    public void move() {
        System.out.println(name + " is moving");
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing " + name);
    }
}

// Interface extending another interface
interface Shape extends Drawable, Movable {
    double getArea();
}

class Rectangle implements Shape {
    private double width;
    private double height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing Rectangle");
    }
    
    @Override
    public void move() {
        System.out.println("Moving Rectangle");
    }
    
    @Override
    public double getArea() {
        return width * height;
    }
}

public class InterfaceDemo {
    public static void main(String[] args) {
        // Using interface reference
        Drawable drawable = new Circle(5);
        drawable.draw();
        drawable.display();  // default method
        
        Drawable.printMessage();  // static method
        
        // Using implementation
        Animal animal = new Animal("Dog");
        animal.move();
        animal.draw();
        
        // Using shape
        Rectangle rect = new Rectangle(4, 5);
        rect.draw();
        rect.move();
        System.out.println("Area: " + rect.getArea());
    }
}
```

## 20.2 Interface vs Class

| Aspect | Interface | Class |
|-------|-----------|-------|
| Implementation | Cannot be instantiated | Can be instantiated |
| Methods | Abstract (default in Java 8+) | Concrete |
| Variables | Constants only | Any type |
| Inheritance | Can extend multiple interfaces | Can extend only one class |
| Multiple | Can implement multiple | Single only |
| Purpose | Contract/specification | Implementation |

---

# 21. Exception Handling

## 21.1 Exception Fundamentals

```java
import java.util.Scanner;

class ExceptionDemo {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        
        // ArrayIndexOutOfBoundsException
        try {
            System.out.println(arr[10]);  // This will throw exception
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index out of bounds: " + e.getMessage());
        }
        
        // ArithmeticException
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic error: " + e.getMessage());
        }
        
        // NullPointerException
        try {
            String str = null;
            System.out.println(str.length());
        } catch (NullPointerException e) {
            System.out.println("Null pointer: " + e.getMessage());
        }
        
        // NumberFormatException
        try {
            int num = Integer.parseInt("abc");
        } catch (NumberFormatException e) {
            System.out.println("Number format error: " + e.getMessage());
        }
        
        // Multiple catch blocks
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter number: ");
            int num = scanner.nextInt();
            System.out.println("Result: " + (10 / num));
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
```

## 21.2 Custom Exceptions

```java
// Custom exception class
class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

// Custom runtime exception
class InvalidMarksException extends RuntimeException {
    public InvalidMarksException(String message) {
        super(message);
    }
}

class Person {
    private String name;
    private int age;
    
    public void setAge(int age) throws InvalidAgeException {
        if (age < 0 || age > 150) {
            throw new InvalidAgeException("Age must be between 0 and 150");
        }
        this.age = age;
    }
    
    public void setMarks(double marks) {
        if (marks < 0 || marks > 100) {
            throw new InvalidMarksException("Marks must be between 0 and 100");
        }
    }
    
    public int getAge() {
        return age;
    }
}

public class CustomExceptionDemo {
    public static void main(String[] args) {
        Person person = new Person();
        
        // Try-catch for checked exception
        try {
            person.setAge(250);
        } catch (InvalidAgeException e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        // Runtime exception (no catch required but can catch)
        try {
            person.setMarks(-10);
        } catch (InvalidMarksException e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        // Try-with-resources
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter name: ");
            String name = scanner.nextLine();
            System.out.println("Name: " + name);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

## 21.3 throw vs throws

```java
class ThrowThrowsDemo {
    // throws: declares exception that may be thrown
    public static int divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return a / b;
    }
    
    // Multiple exceptions
    public static void process(String str) throws NullPointerException, 
                                            NumberFormatException {
        if (str == null) {
            throw new NullPointerException("String is null");
        }
        int num = Integer.parseInt(str);
        System.out.println("Number: " + num);
    }
    
    public static void main(String[] args) {
        try {
            System.out.println(divide(10, 0));
            process("abc");
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (NullPointerException | NumberFormatException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

---

# 22. String Handling

## 22.1 String Methods

```java
public class StringMethodsDemo {
    public static void main(String[] args) {
        String str = "Hello World";
        
        // Length
        System.out.println("Length: " + str.length());
        
        // Character at index
        System.out.println("Char at 0: " + str.charAt(0));
        
        // Substring
        System.out.println("Substring (0, 5): " + str.substring(0, 5));
        System.out.println("Substring from 6: " + str.substring(6));
        
        // Concatenation
        String str2 = str.concat("!!!");
        System.out.println("Concatenated: " + str2);
        
        // Replace
        System.out.println("Replace 'World' with 'Java': " + str.replace("World", "Java"));
        
        // toUpperCase and toLowerCase
        System.out.println("Uppercase: " + str.toUpperCase());
        System.out.println("Lowercase: " + str.toLowerCase());
        
        // Trim (removes whitespace from both ends)
        String str3 = "   Hello   ";
        System.out.println("Trimmed: '" + str3.trim() + "'");
        
        // Split
        String text = "apple,banana,orange";
        String[] fruits = text.split(",");
        System.out.println("Splitted:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
        
        // Index of
        System.out.println("Index of 'World': " + str.indexOf("World"));
        System.out.println("Index of 'l': " + str.indexOf('l'));
        System.out.println("Last index of 'l': " + str.lastIndexOf('l'));
        
        // Contains
        System.out.println("Contains 'World': " + str.contains("World"));
        
        // StartsWith and endsWith
        System.out.println("Starts with 'Hello': " + str.startsWith("Hello"));
        System.out.println("Ends with 'World': " + str.endsWith("World"));
        
        // equals and equalsIgnoreCase
        String s1 = "hello";
        String s2 = "HELLO";
        System.out.println("equals: " + s1.equals(s2));
        System.out.println("equalsIgnoreCase: " + s1.equalsIgnoreCase(s2));
        
        // CompareTo
        System.out.println("compareTo: " + s1.compareTo("hellp"));
        
        // Is empty
        String empty = "";
        System.out.println("Is empty: " + empty.isEmpty());
        
        // StringBuilder
        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" World");
        sb.insert(5, "!");
        sb.reverse();
        System.out.println("\nStringBuilder: " + sb);
    }
}
```

---

# 23. Multithreaded Programming

## 23.1 Creating Threads

```java
// Method 1: Extending Thread class
class MyThread extends Thread {
    private String threadName;
    
    public MyThread(String name) {
        this.threadName = name;
    }
    
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(threadName + ": " + i);
            try {
                Thread.sleep(500);  // Pause for 500ms
            } catch (InterruptedException e) {
                System.out.println("Thread interrupted");
            }
        }
    }
}

// Method 2: Implementing Runnable interface
class MyRunnable implements Runnable {
    private String threadName;
    
    public MyRunnable(String name) {
        this.threadName = name;
    }
    
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(threadName + ": " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println("Thread interrupted");
            }
        }
    }
}

// Thread synchronization example
class SharedResource {
    private int count = 0;
    
    // Synchronized method - only one thread can access at a time
    public synchronized void increment() {
        count++;
        System.out.println(Thread.currentThread().getName() + ": " + count);
    }
    
    public int getCount() {
        return count;
    }
}

class SyncThread implements Runnable {
    private SharedResource resource;
    
    public SyncThread(SharedResource resource) {
        this.resource = resource;
    }
    
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            resource.increment();
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        // Method 1: Extending Thread
        MyThread thread1 = new MyThread("Thread-1");
        thread1.start();
        
        // Method 2: Using Runnable
        Runnable runnable = new MyRunnable("Thread-2");
        Thread thread2 = new Thread(runnable);
        thread2.start();
        
        // Main thread continues
        for (int i = 1; i <= 5; i++) {
            System.out.println("Main: " + i);
        }
        
        // Synchronization example
        System.out.println("\n=== Synchronization ===");
        SharedResource resource = new SharedResource();
        Thread t1 = new Thread(new SyncThread(resource), "T1");
        Thread t2 = new Thread(new SyncThread(resource), "T2");
        t1.start();
        t2.start();
    }
}
```

## 23.2 Thread Methods

```java
class ThreadMethodsDemo {
    public static void main(String[] args) {
        Thread.currentThread().setName("Main Thread");
        
        System.out.println("Thread Name: " + Thread.currentThread().getName());
        System.out.println("Thread Priority: " + Thread.currentThread().getPriority());
        
        Thread thread = new Thread(() -> {
            System.out.println("New thread started");
            System.out.println("Is Daemon: " + Thread.currentThread().isDaemon());
        }, "New Thread");
        
        System.out.println("Before start - Alive: " + thread.isAlive());
        thread.start();
        System.out.println("After start - Alive: " + thread.isAlive());
        
        try {
            thread.join();  // Wait for thread to complete
        } catch (InterruptedException e) {
            System.out.println("Interrupted");
        }
        
        System.out.println("After join - Alive: " + thread.isAlive());
        
        // Creating daemon thread
        Thread daemon = new Thread(() -> {
            System.out.println("Daemon running");
        });
        daemon.setDaemon(true);
        daemon.start();
        
        System.out.println("Is Daemon: " + daemon.isDaemon());
    }
}
```

---

# 24. Java Input/Output

## 24.1 Console I/O

```java
import java.util.Scanner;
import java.io.*;

public class ConsoleIO {
    public static void main(String[] args) {
        // Scanner for reading input
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        
        System.out.print("Enter your GPA: ");
        double gpa = scanner.nextDouble();
        
        System.out.println("\n=== User Information ===");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("GPA: " + gpa);
        
        scanner.close();
        
        // Using BufferedReader
        System.out.println("\n=== BufferedReader ===");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.print("Enter something: ");
            String input = reader.readLine();
            System.out.println("You entered: " + input);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## 24.2 File I/O

```java
import java.io.*;

public class FileIO {
    // Writing to file
    public static void writeToFile(String filename) {
        try (FileWriter writer = new FileWriter(filename)) {
            writer.write("Hello World\n");
            writer.write("This is second line\n");
            writer.write("Number: " + 42);
            System.out.println("Written to file successfully");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    // Reading from file
    public static void readFromFile(String filename) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            System.out.println("\n=== File Content ===");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    // File operations
    public static void fileOperations(String filename) {
        File file = new File(filename);
        
        System.out.println("\n=== File Operations ===");
        System.out.println("Exists: " + file.exists());
        System.out.println("Is File: " + file.isFile());
        System.out.println("Is Directory: " + file.isDirectory());
        System.out.println("Absolute Path: " + file.getAbsolutePath());
        System.out.println("Can Read: " + file.canRead());
        System.out.println("Can Write: " + file.canWrite());
        System.out.println("Length: " + file.length());
    }
    
    public static void main(String[] args) {
        String filename = "test.txt";
        
        writeToFile(filename);
        readFromFile(filename);
        fileOperations(filename);
        
        // Using FileInputStream and FileOutputStream
        try (FileInputStream fis = new FileInputStream(filename);
             FileOutputStream fos = new FileOutputStream("copy.txt")) {
            
            int data;
            while ((data = fis.read()) != -1) {
                fos.write(data);
            }
            System.out.println("\nFile copied successfully");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

---

# 25. Collection Framework

## 25.1 List Implementations

```java
import java.util.*;

public class ListDemo {
    public static void main(String[] args) {
        // ArrayList
        System.out.println("=== ArrayList ===");
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("Apple");
        arrayList.add("Banana");
        arrayList.add("Cherry");
        arrayList.add(1, "Mango");  // Insert at index
        
        System.out.println("ArrayList: " + arrayList);
        System.out.println("Size: " + arrayList.size());
        System.out.println("Get: " + arrayList.get(2));
        System.out.println("Contains: " + arrayList.contains("Apple"));
        System.out.println("Index of: " + arrayList.indexOf("Banana"));
        
        // LinkedList
        System.out.println("\n=== LinkedList ===");
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.add(10);
        linkedList.add(20);
        linkedList.addFirst(5);    // Add at beginning
        linkedList.addLast(30);   // Add at end
        
        System.out.println("LinkedList: " + linkedList);
        System.out.println("First: " + linkedList.getFirst());
        System.out.println("Last: " + linkedList.getLast());
        
        // Iterating
        System.out.println("\n=== Iterating ===");
        for (String item : arrayList) {
            System.out.println(item);
        }
        
        // Using Iterator
        System.out.println("\nUsing Iterator:");
        Iterator<String> iterator = arrayList.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        
        // Vector (synchronized)
        System.out.println("\n=== Vector ===");
        Vector<String> vector = new Vector<>();
        vector.add("One");
        vector.add("Two");
        System.out.println("Vector: " + vector);
    }
}
```

## 25.2 Set Implementations

```java
import java.util.*;

public class SetDemo {
    public static void main(String[] args) {
        // HashSet (unordered, no duplicates)
        System.out.println("=== HashSet ===");
        HashSet<Integer> hashSet = new HashSet<>();
        hashSet.add(10);
        hashSet.add(20);
        hashSet.add(10);  // Duplicate - ignored
        hashSet.add(30);
        
        System.out.println("HashSet: " + hashSet);
        
        // LinkedHashSet (maintains insertion order)
        System.out.println("\n=== LinkedHashSet ===");
        LinkedHashSet<String> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add("First");
        linkedHashSet.add("Second");
        linkedHashSet.add("Third");
        
        System.out.println("LinkedHashSet: " + linkedHashSet);
        
        // TreeSet (sorted, balanced tree)
        System.out.println("\n=== TreeSet ===");
        TreeSet<String> treeSet = new TreeSet<>();
        treeSet.add("Banana");
        treeSet.add("Apple");
        treeSet.add("Cherry");
        
        System.out.println("TreeSet: " + treeSet);
        System.out.println("First: " + treeSet.first());
        System.out.println("Last: " + treeSet.last());
        System.out.println("Lower: " + treeSet.lower("Cherry"));
        System.out.println("Higher: " + treeSet.higher("Apple"));
        
        // HashSet with custom object
        System.out.println("\n=== Custom Object in Set ===");
        HashSet<Person> personSet = new HashSet<>();
        personSet.add(new Person("John", 25));
        personSet.add(new Person("Jane", 30));
        personSet.add(new Person("John", 25));  // Duplicate if equals/hashCode implemented
        
        System.out.println("Person set size: " + personSet.size());
    }
}

class Person {
    String name;
    int age;
    
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    @Override
    public int hashCode() {
        return name.hashCode() + age;
    }
    
    @Override
    public boolean equals(Object obj) {
        Person p = (Person) obj;
        return this.name.equals(p.name) && this.age == p.age;
    }
    
    @Override
    public String toString() {
        return name + "-" + age;
    }
}
```

## 25.3 Map Implementations

```java
import java.util.*;

public class MapDemo {
    public static void main(String[] args) {
        // HashMap (key-value pairs, no duplicates)
        System.out.println("=== HashMap ===");
        HashMap<String, Integer> hashMap = new HashMap<>();
        hashMap.put("Apple", 100);
        hashMap.put("Banana", 50);
        hashMap.put("Orange", 80);
        hashMap.put("Mango", 120);
        
        System.out.println("HashMap: " + hashMap);
        System.out.println("Get: " + hashMap.get("Apple"));
        System.out.println("Contains key: " + hashMap.containsKey("Banana"));
        System.out.println("Contains value: " + hashMap.containsValue(100));
        
        // Update value
        hashMap.put("Apple", 150);
        System.out.println("After update: " + hashMap.get("Apple"));
        
        // Remove
        hashMap.remove("Orange");
        System.out.println("After remove: " + hashMap);
        
        // TreeMap (sorted by keys)
        System.out.println("\n=== TreeMap ===");
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("Zebra", 200);
        treeMap.put("Apple", 100);
        treeMap.put("Cat", 50);
        
        System.out.println("TreeMap: " + treeMap);
        System.out.println("First key: " + treeMap.firstKey());
        System.out.println("Last key: " + treeMap.lastKey());
        
        // LinkedHashMap (maintains insertion order)
        System.out.println("\n=== LinkedHashMap ===");
        LinkedHashMap<String, String> linkedMap = new LinkedHashMap<>();
        linkedMap.put("One", "First");
        linkedMap.put("Two", "Second");
        linkedMap.put("Three", "Third");
        
        System.out.println("LinkedHashMap: " + linkedMap);
        
        // Iterating Map
        System.out.println("\n=== Iterating Map ===");
        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
```

## 25.4 Queue and Deque

```java
import java.util.*;

public class QueueDemo {
    public static void main(String[] args) {
        // PriorityQueue (min-heap by default)
        System.out.println("=== PriorityQueue ===");
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(30);
        pq.add(10);
        pq.add(50);
        pq.add(20);
        
        System.out.print("PQ: ");
        while (!pq.isEmpty()) {
            System.out.print(pq.poll() + " ");
        }
        
        // LinkedList as Queue
        System.out.println("\n\n=== LinkedList Queue ===");
        Queue<String> queue = new LinkedList<>();
        queue.add("First");
        queue.add("Second");
        queue.add("Third");
        
        System.out.println("Queue: " + queue);
        System.out.println("Peek: " + queue.peek());
        System.out.println("Poll: " + queue.poll());
        System.out.println("After poll: " + queue);
        
        // Deque (double-ended queue)
        System.out.println("\n=== Deque ===");
        Deque<Integer> deque = new ArrayDeque<>();
        deque.addFirst(10);
        deque.addLast(20);
        deque.addFirst(5);
        deque.addLast(25);
        
        System.out.println("Deque: " + deque);
        System.out.println("First: " + deque.getFirst());
        System.out.println("Last: " + deque.getLast());
    }
}
```

---

# Quick Reference Summary

## Java OOP Key Concepts

| Concept | Description |
|---------|-------------|
| **Encapsulation** | Hiding data with access modifiers and getters/setters |
| **Inheritance** | Acquiring properties from parent class using `extends` |
| **Polymorphism** | Same interface, different implementations |
| **Abstraction** | Hiding complexity with abstract classes/interfaces |
| **Interface** | Contract with abstract methods (100% abstract until Java 8) |
| **Abstract Class** | Cannot be instantiated, can have both abstract and concrete methods |

## Access Modifiers

- `public`: Accessible everywhere
- `protected`: Accessible within package and subclasses
- `default` (package-private): Accessible within package
- `private`: Accessible only within the class

## Keywords

- `static`: Class-level members (shared)
- `final`: Constant (cannot change)
- `abstract`: Incomplete (must be implemented)
- `super`: Reference to parent class
- `this`: Reference to current object

## Exception Hierarchy

```
Throwable
├── Error
└── Exception
    ├── RuntimeException (unchecked)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   └── ArithmeticException
    └── Checked Exceptions
        ├── IOException
        └── FileNotFoundException
```

---

*This complete guide covers all topics from your Java OOP syllabus with theory and practical code examples. Practice these examples to master Java programming concepts.*