# Java Object-Oriented Programming Complete Notes

A comprehensive reference covering all Java OOP topics — theory-first, with focused code snippets.

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

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around **objects** — self-contained units that combine data (attributes) and behavior (methods). Instead of writing a sequence of instructions, you model the real world as interacting objects.

The shift from procedural to object-oriented thinking is fundamental:
- **Procedural**: "What does the program do?" → focuses on functions and logic flow
- **Object-Oriented**: "What does the program model?" → focuses on entities and their relationships

### Key Characteristics of OOP:
- **Abstraction**: Expose only what is necessary; hide internal complexity. A car's steering wheel abstracts the steering mechanism.
- **Encapsulation**: Bundle data and the methods that operate on it into one unit, and protect data from unauthorized access.
- **Inheritance**: Let a new class reuse and extend the structure of an existing class, establishing an IS-A relationship.
- **Polymorphism**: Allow one interface to represent different underlying types, enabling flexible and extensible code.

## 1.2 History of OOP

| Year | Milestone |
|------|-----------|
| 1967 | **Simula** — first language with class and object concepts |
| 1972 | **Smalltalk** — introduced message passing and pure OOP |
| 1983 | **C++** — brought OOP to systems programming |
| 1991 | **Java** design begun by James Gosling at Sun Microsystems |
| 1995 | **Java 1.0** released — platform-independent OOP for the masses |
| 2014+ | **Java 8/11/17** — modern features like lambdas, records, sealed classes |

---

# 2. OOP Principles

## 2.1 Encapsulation

### Theory

Encapsulation is the practice of **wrapping data and methods into a single unit (class)** and **restricting direct access** to an object's internal state. External code interacts only through a well-defined public interface.

Key ideas:
- **Data Hiding**: Fields are declared `private`. No outside code can read or write them directly.
- **Controlled Access**: `public` getter and setter methods act as gatekeepers, allowing validation before any change is made.
- **Loose Coupling**: If the internal representation changes, only the class itself needs to be updated — callers remain unaffected.
- **Maintainability**: Encapsulated code is easier to test, debug, and refactor in isolation.

A real-world analogy: a vending machine exposes buttons (public interface) but hides its internal motor and cash mechanism (private state).

### Example Code:
```java
class BankAccount {
    private double balance;  // hidden from outside

    public BankAccount(double initial) { balance = initial; }

    public double getBalance() { return balance; }

    public void deposit(double amount) {
        if (amount > 0) balance += amount;  // validated before change
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) balance -= amount;
    }
}
```

---

## 2.2 Inheritance

### Theory

Inheritance allows a **child (sub) class** to acquire the fields and methods of a **parent (super) class**. It models the IS-A relationship and promotes code reuse.

Key ideas:
- **extends** keyword links child to parent in Java.
- The child inherits all non-private members of the parent.
- The child can **add** new fields/methods and **override** existing ones.
- **Constructor chaining**: A child constructor must call `super(...)` as its first statement if the parent lacks a no-arg constructor.
- **Types of Inheritance**:
  - *Single*: One parent → one child
  - *Multilevel*: A → B → C (chain)
  - *Hierarchical*: One parent → multiple children
  - *Multiple* (via interfaces): A class implements several interfaces

Java does **not** support multiple class inheritance to avoid the *Diamond Problem* — ambiguity when two parents define the same method.

### Example Code:
```java
class Animal {
    protected String name;
    Animal(String name) { this.name = name; }
    void eat() { System.out.println(name + " eats"); }
}

class Dog extends Animal {
    Dog(String name) { super(name); }          // chain to parent
    void bark() { System.out.println(name + " barks"); }
}

// Usage
Dog d = new Dog("Rex");
d.eat();   // inherited
d.bark();  // own method
```

---

## 2.3 Polymorphism

### Theory

Polymorphism ("many forms") lets a single interface represent different underlying implementations. It makes code generic, extensible, and easier to maintain.

Two types:
- **Compile-time (Static) Polymorphism** — resolved at compile time via *method overloading*. The compiler picks the right method based on the argument types.
- **Runtime (Dynamic) Polymorphism** — resolved at runtime via *method overriding*. A parent reference holds a child object; the JVM calls the child's overridden method.

Key mechanism — **Dynamic Method Dispatch**: when `parent.method()` is called and `parent` actually refers to a child object, Java invokes the child's version of `method()` at runtime, not the parent's.

Upcasting (parent ref ← child object) is automatic and safe. Downcasting (back to child type) requires explicit casting and can throw `ClassCastException`.

### Example Code:
```java
class Shape {
    void draw() { System.out.println("Drawing shape"); }
}

class Circle extends Shape {
    @Override
    void draw() { System.out.println("Drawing circle"); }
}

class Square extends Shape {
    @Override
    void draw() { System.out.println("Drawing square"); }
}

// Runtime polymorphism
Shape[] shapes = { new Circle(), new Square() };
for (Shape s : shapes) s.draw();  // dispatched at runtime
```

---

# 3. Java as an Object-Oriented Language

## 3.1 Java Features

### Pure Object-Oriented:
- Every piece of code lives inside a class — no standalone functions.
- Even primitives have corresponding **wrapper classes** (`Integer`, `Double`, etc.) for when object behavior is needed.
- Java is not *purely* OOP (primitives exist for performance), but is considered *strongly* OOP.

### Platform Independent — Write Once, Run Anywhere:
- Java source (`.java`) is compiled by `javac` into **bytecode** (`.class`).
- Bytecode is a platform-neutral intermediate representation, not native machine code.
- The **JVM (Java Virtual Machine)** on each OS interprets or JIT-compiles bytecode to native instructions.
- This means the same `.class` file runs unchanged on Windows, Linux, and macOS.

### Other Key Features:
| Feature | Description |
|---------|-------------|
| **Simple** | No pointers, automatic memory management (GC) |
| **Robust** | Strong type checking, exception handling |
| **Secure** | No direct memory access; sandbox model |
| **Multithreaded** | Built-in `Thread` and `synchronized` support |
| **Distributed** | Designed with networking APIs (RMI, Sockets) |
| **High Performance** | JIT compilation at runtime |

## 3.2 Java Bytecode

```
Source Code (.java)
      |
   javac (compiler)
      |
  Bytecode (.class)
      |
   JVM (per OS)
      |
  Native execution
```

```java
// HelloWorld.java  →  javac HelloWorld.java  →  java HelloWorld
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

## 3.3 Internet-Enabled Language

Java was designed from the ground up for networked environments:
- **Applets**: Java programs embedded in web pages (legacy)
- **Servlets & JSP**: Server-side web processing
- **RMI** (Remote Method Invocation): Call methods on objects in other JVMs across a network
- **Java EE / Jakarta EE**: Full enterprise platform for web services, messaging, persistence
- **Security Manager**: Fine-grained permission model for downloaded code

---

# 4. Data Types, Variables, and Operators

## 4.1 Data Types

### Primitive Data Types (8 types):

| Type | Size | Default | Range / Notes |
|------|------|---------|---------------|
| `byte` | 8-bit | 0 | –128 to 127 |
| `short` | 16-bit | 0 | –32,768 to 32,767 |
| `int` | 32-bit | 0 | ~±2.1 billion |
| `long` | 64-bit | 0L | ~±9.2 × 10¹⁸ |
| `float` | 32-bit | 0.0f | 6–7 decimal digits precision |
| `double` | 64-bit | 0.0d | 15–16 decimal digits precision |
| `char` | 16-bit | `'\u0000'` | Unicode 0–65,535 |
| `boolean` | JVM-defined | `false` | `true` / `false` only |

### Reference Data Types:
- **Class** types: `String`, `Scanner`, user-defined classes
- **Interface** types: variables of interface type hold objects that implement it
- **Array** types: `int[]`, `String[][]`, etc.
- Reference variables store a **memory address**, not the value itself
- Default value for any reference variable is `null`

### Example Code:
```java
int age = 25;
double gpa = 3.85;
char grade = 'A';
boolean passed = true;
String name = "Alice";   // reference type

System.out.println(name + " | Age: " + age + " | GPA: " + gpa);
```

---

## 4.2 Variables

### Types of Variables:

| Type | Declared In | Scope | Lifetime |
|------|-------------|-------|----------|
| **Instance** | Class body (no `static`) | Whole object | Object lifetime |
| **Static** | Class body with `static` | Whole class | Program lifetime |
| **Local** | Inside a method/block | That method/block | Method execution |
| **Parameter** | Method signature | That method | Method execution |

Key rules:
- Local variables **must be initialized** before use (no default).
- Instance and static variables get default values (0, false, null).
- A local variable can **shadow** an instance variable; use `this.x` to distinguish.

### Example Code:
```java
class Counter {
    static int total = 0;   // static — shared
    int count;              // instance — per object

    void increment() {
        int step = 1;       // local
        count += step;
        total += step;
    }
}
```

---

## 4.3 Operators

### Summary Table:

| Category | Operators | Notes |
|----------|-----------|-------|
| Arithmetic | `+ - * / %` | `/` on ints truncates |
| Unary | `++ -- + - !` | Pre vs post increment matters |
| Relational | `== != > < >= <=` | Returns `boolean` |
| Logical | `&& \|\| !` | Short-circuit evaluation |
| Bitwise | `& \| ^ ~ << >>` | Operate on binary bits |
| Assignment | `= += -= *= /= %=` | Compound shorthand |
| Ternary | `condition ? a : b` | Inline if-else |

```java
int a = 10, b = 3;
System.out.println(a / b);          // 3  (integer division)
System.out.println(a % b);          // 1
System.out.println(a > b && b > 0); // true (short-circuit &&)
System.out.println(a > 5 ? "big" : "small"); // big
System.out.println(a & b);          // 2  (bitwise AND: 1010 & 0011)
```

**Short-circuit evaluation**: In `A && B`, if A is false, B is never evaluated. In `A || B`, if A is true, B is skipped. This is important when B has side effects or could throw an exception.

---

# 5. Control Statements

## 5.1 Decision Making Statements

### Theory:
Control statements alter the sequential flow of execution. Java provides:
- `if / if-else / if-else-if` ladder — condition-based branching
- `switch` — multi-way branch on a discrete value (supports `int`, `char`, `String`, `enum`)
- **Switch expression** (Java 14+) — returns a value using `->` syntax, no fall-through by default

The `switch` statement has **fall-through** behavior by default: without `break`, execution continues into the next case.

### if-else:
```java
int marks = 75;
if (marks >= 90)       System.out.println("A+");
else if (marks >= 75)  System.out.println("B");
else                   System.out.println("C");
```

### switch:
```java
int day = 3;
switch (day) {
    case 1: System.out.println("Mon"); break;
    case 2: System.out.println("Tue"); break;
    case 3: System.out.println("Wed"); break;
    default: System.out.println("Other");
}

// Switch expression (Java 14+)
String label = switch (day) {
    case 1 -> "Mon";
    case 2 -> "Tue";
    default -> "Other";
};
```

---

## 5.2 Loop Statements

### Theory:
Loops repeat a block of code while a condition holds. Java offers:
- **for**: best when the number of iterations is known in advance
- **while**: best when the condition controls iteration
- **do-while**: guarantees **at least one execution** regardless of the condition
- **enhanced for** (for-each): cleanly iterates over arrays and collections

All loops can be nested. Deep nesting harms readability — prefer helper methods.

```java
// for loop
for (int i = 0; i < 3; i++) System.out.print(i + " ");  // 0 1 2

// while loop
int n = 5;
while (n > 0) { System.out.print(n + " "); n--; }       // 5 4 3 2 1

// do-while (always runs once)
do { System.out.println("runs once even if false"); } while (false);

// for-each
int[] arr = {10, 20, 30};
for (int x : arr) System.out.print(x + " ");            // 10 20 30
```

---

## 5.3 Jump Statements

### Theory:
- `break` — immediately exits the nearest enclosing loop or switch
- `continue` — skips the rest of the current iteration and jumps to the next
- `return` — exits the current method, optionally returning a value
- **Labeled break/continue** — exits or continues an outer loop by referring to its label

```java
// break
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    System.out.print(i + " ");   // 0 1 2 3 4
}

// continue (skip even numbers)
for (int i = 0; i < 6; i++) {
    if (i % 2 == 0) continue;
    System.out.print(i + " ");   // 1 3 5
}

// labeled break (exit outer loop)
outer:
for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
        if (j == 1) break outer;
```

---

# 6. Type Conversion and Casting

## 6.1 Widening (Automatic) Conversion

### Theory:
Java automatically promotes a smaller type to a larger compatible type. No data is lost:

```
byte → short → int → long → float → double
                char ↗
```

The compiler handles this implicitly. This is also called **implicit casting** or **upcasting** for primitives.

```java
int i = 100;
double d = i;     // automatic: int → double
System.out.println(d);  // 100.0

char c = 'A';
int code = c;     // char → int (ASCII value)
System.out.println(code);  // 65
```

---

## 6.2 Narrowing (Explicit) Casting

### Theory:
Converting from a larger type to a smaller one **may lose data** and must be done explicitly using a cast operator `(type)`. The programmer takes responsibility for any loss.

- **Truncation**: fractional parts are dropped (not rounded)
- **Overflow**: if the value exceeds the target type's range, bits wrap around unexpectedly

```java
double d = 9.99;
int i = (int) d;       // truncates: i = 9 (not 10)

int big = 130;
byte b = (byte) big;   // overflow: 130 > 127, b = -126

// Casting for correct division
int x = 7, y = 2;
double result = (double) x / y;  // 3.5 (without cast: 3)
```

---

# 7. Classes and Objects

## 7.1 Class Definition

### Theory:
A **class** is a blueprint — it defines what data an object holds (fields) and what it can do (methods). No memory is allocated for data until an **object** (instance) is created with `new`.

Important concepts:
- **Fields** (instance variables): each object gets its own copy
- **Methods**: define behavior; can read/modify fields
- **`this` keyword**: refers to the current object instance; used to disambiguate field names from parameter names
- **Object**: created on the **heap**; the variable holds a **reference** (address) to it
- Two reference variables can point to the **same** object — changes through one are visible through the other

```java
class Student {
    String name;
    int marks;

    Student(String name, int marks) {
        this.name = name;     // 'this' resolves ambiguity
        this.marks = marks;
    }

    void display() {
        System.out.println(name + " scored " + marks);
    }
}

Student s1 = new Student("Ana", 90);
Student s2 = s1;          // both point to same object
s1.display();             // Ana scored 90
s2.marks = 95;
s1.display();             // Ana scored 95 (same object!)
```

---

# 8. Methods

## 8.1 Method Definition and Calling

### Theory:
A method encapsulates a reusable block of logic. Key parts of a method signature:
- **Return type**: what it gives back (`void` = nothing)
- **Name**: identifier (camelCase by convention)
- **Parameters**: typed input values (pass-by-value in Java)
- **Body**: the logic

Methods promote **DRY** (Don't Repeat Yourself) and **SRP** (Single Responsibility Principle).

```java
class MathHelper {
    int square(int n) { return n * n; }
    double average(int a, int b) { return (a + b) / 2.0; }
}

MathHelper h = new MathHelper();
System.out.println(h.square(5));       // 25
System.out.println(h.average(4, 7));   // 5.5
```

## 8.2 Static Methods

### Theory:
`static` methods belong to the **class**, not to any instance. They:
- Can be called without creating an object: `ClassName.method()`
- Cannot access instance fields or call instance methods directly (no `this` reference)
- Are ideal for **utility functions** (e.g., `Math.sqrt()`, `Arrays.sort()`)

```java
class Utils {
    static int max(int a, int b) { return a > b ? a : b; }
}

System.out.println(Utils.max(8, 3));  // 8 — no object needed
```

---

# 9. Constructors

## 9.1 Constructor Basics

### Theory:
A **constructor** is a special method invoked automatically when an object is created with `new`. It initializes the object's state.

Key rules:
- Same name as the class, **no return type** (not even `void`)
- If you define no constructor, Java provides a **default no-arg constructor**
- If you define any constructor, the default is **no longer provided**
- Constructors can be **overloaded** (multiple constructors, different parameter lists)
- A constructor can call another constructor of the same class using `this(...)` — called **constructor chaining**
- A **copy constructor** takes an object of the same class and copies its state

```java
class Box {
    double w, h, d;

    Box()                        { this(1, 1, 1); }       // chains to below
    Box(double w, double h, double d) { this.w=w; this.h=h; this.d=d; }
    Box(Box b)                   { this(b.w, b.h, b.d); } // copy constructor

    double volume() { return w * h * d; }
}

Box b1 = new Box();          // 1×1×1  → vol = 1.0
Box b2 = new Box(3, 4, 5);  // 3×4×5  → vol = 60.0
Box b3 = new Box(b2);       // copy   → vol = 60.0
```

---

# 10. Access Control and Encapsulation

## 10.1 Access Modifiers

### Theory:
Access modifiers control **visibility** of classes, fields, and methods. They are the enforcement mechanism of encapsulation.

| Modifier | Same Class | Same Package | Subclass | Anywhere |
|----------|-----------|--------------|----------|----------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| *(default)* | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

Design guidelines:
- Make fields **private** by default; expose only what is needed
- Use **protected** for members that subclasses need to use or override
- Use **public** only for the intended API surface
- **default** (package-private) is useful for internal package helpers

```java
class Person {
    private String name;       // hidden
    protected int age;         // subclasses can access
    public String country;     // open to all

    public String getName() { return name; }      // controlled read
    public void setName(String n) { name = n; }   // controlled write
}
```

---

# 11. static and final Keywords

## 11.1 static Keyword

### Theory:
`static` members are associated with the **class itself**, not with any particular instance.

- **Static field**: One copy shared by all instances. Useful for counters, constants, singletons.
- **Static method**: Utility behavior that doesn't need object state.
- **Static block**: Runs once when the class is loaded by the JVM — used for complex static initialization.
- **Static nested class**: A nested class that doesn't need a reference to the outer instance.

```java
class Student {
    static int count = 0;   // shared across all objects
    String name;

    Student(String name) { this.name = name; count++; }
    static int getCount() { return count; }
}

new Student("Ana");
new Student("Bob");
System.out.println(Student.getCount()); // 2
```

---

## 11.2 final Keyword

### Theory:
`final` means **"cannot be changed after assignment"**. It applies to three things:

- **final variable**: becomes a constant; must be assigned exactly once (can be in constructor for instance finals)
- **final method**: cannot be overridden in any subclass
- **final class**: cannot be subclassed at all (e.g., `String`, `Integer` in Java are final)

Using `final` communicates design intent clearly and allows compiler/JVM optimizations.

```java
final class Immutable {           // cannot extend this
    final double PI = 3.14159;    // constant field

    final void show() {           // cannot override
        System.out.println("PI = " + PI);
    }
}
```

---

# 12. Method Overloading

### Theory:
**Method overloading** is compile-time (static) polymorphism — multiple methods in the same class share a name but differ in:
- Number of parameters
- Type of parameters
- Order of parameter types

The return type **alone** is not enough to distinguish overloaded methods. The compiler resolves the correct version at compile time by matching the call signature. Overloading improves API usability — callers use one intuitive name regardless of input type.

```java
class Print {
    void show(int x)    { System.out.println("int: " + x); }
    void show(double x) { System.out.println("double: " + x); }
    void show(String x) { System.out.println("String: " + x); }
    void show(int x, int y) { System.out.println("sum: " + (x+y)); }
}

Print p = new Print();
p.show(5);       // int: 5
p.show(3.14);    // double: 3.14
p.show("hi");    // String: hi
p.show(2, 3);    // sum: 5
```

---

# 13. Parameter Passing and Recursion

## 13.1 Call by Value

### Theory:
Java is **strictly pass-by-value**:
- For **primitives**: a copy of the value is passed; the original is unchanged.
- For **objects**: a copy of the **reference** (address) is passed. The method can mutate the object's state through that reference, but it cannot make the caller's variable point to a different object.

This is a common source of confusion — objects *seem* to be passed by reference, but reassigning the parameter inside the method has no effect on the caller.

```java
void change(int x) { x = 99; }          // won't affect caller's int
void append(StringBuilder sb) {
    sb.append(" World");                 // mutates the same object
}

int n = 5;
change(n);
System.out.println(n);  // still 5

StringBuilder s = new StringBuilder("Hello");
append(s);
System.out.println(s);  // Hello World
```

---

## 13.2 Recursion

### Theory:
A method that **calls itself** is recursive. Every recursive solution has:
1. **Base case**: the condition that stops recursion (prevents infinite loop)
2. **Recursive case**: the call that breaks the problem into a smaller subproblem

Recursion trades **stack space** for code simplicity. Each call pushes a new frame on the call stack. Too many calls without a base case causes a `StackOverflowError`. For performance-sensitive code, iterative solutions are generally preferred.

```java
int factorial(int n) {
    if (n <= 1) return 1;            // base case
    return n * factorial(n - 1);     // recursive case
}

int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

System.out.println(factorial(5));    // 120
System.out.println(fib(7));          // 13
```

---

# 14. Nested Classes

## 14.1 Types of Nested Classes

### Theory:
Java allows classes to be defined inside other classes. This is useful for logically grouping classes that are only used in one place.

| Type | `static`? | Access to outer? | Notes |
|------|-----------|-----------------|-------|
| Static nested | Yes | Only static members | Used like a top-level class |
| Inner (non-static) | No | All members including private | Needs outer instance |
| Local | No | Effectively final locals | Defined inside a method |
| Anonymous | No | Effectively final locals | Inline, no class name, one-time use |

Anonymous classes are commonly used to implement interfaces on the fly. Java 8+ lambdas are a cleaner alternative for functional interfaces.

```java
class Outer {
    private int x = 10;

    class Inner {
        void show() { System.out.println(x); }  // accesses outer's private x
    }

    static class Nested {
        void show() { System.out.println("static nested"); }
    }
}

Outer.Nested n = new Outer.Nested();     // no outer instance needed
Outer.Inner i = new Outer().new Inner(); // outer instance required
```

---

# 15. Inheritance

## 15.1 Types of Inheritance

### Theory:
Java supports the following inheritance patterns:

- **Single**: `Dog extends Animal` — straightforward IS-A
- **Multilevel**: `A → B → C` — forms a chain; `C` inherits from both `B` and `A`
- **Hierarchical**: `Dog extends Animal`, `Cat extends Animal` — multiple children, one parent
- **Multiple** (via interfaces only): A class implements `Flyable` and `Swimmable`

Java blocks multiple **class** inheritance to avoid the **Diamond Problem**: if `C extends A, B` and both define `method()`, which version does `C` inherit? Interfaces with default methods handle this with explicit override requirements.

```java
class Animal { void breathe() { System.out.println("breathing"); } }
class Mammal extends Animal { void feed() { System.out.println("feeding young"); } }
class Dog extends Mammal {    void bark()  { System.out.println("woof"); } }

// Multilevel: Dog inherits from Mammal AND Animal
Dog d = new Dog();
d.breathe();  d.feed();  d.bark();
```

---

## 15.2 Using super Keyword

### Theory:
`super` refers to the **parent class** and is used to:
1. Call a parent constructor: `super(args)` — must be the **first line** in the child constructor
2. Call an overridden parent method: `super.method()`
3. Access a hidden parent field: `super.field`

If a child constructor does not explicitly call `super(...)`, the compiler inserts `super()` (no-arg) automatically. If the parent has no no-arg constructor, this causes a compile error.

```java
class Shape { String color; Shape(String c) { color = c; } }

class Circle extends Shape {
    double radius;
    Circle(String c, double r) {
        super(c);        // must be first line
        radius = r;
    }
    void info() {
        System.out.println(color + " circle, r=" + radius);
    }
}
```

---

# 16. Method Overriding

### Theory:
**Method overriding** is runtime (dynamic) polymorphism — a subclass provides its own implementation of a method defined in the parent class.

Rules:
- Same method name, same parameter list, same (or covariant) return type
- Access level cannot be **more restrictive** than the parent's version
- `@Override` annotation is optional but strongly recommended — the compiler catches typos
- `static` and `private` methods cannot be overridden (only hidden)
- A `final` method cannot be overridden

The decision of which version runs is made at **runtime** based on the actual object type, not the reference type — this is **dynamic dispatch**.

```java
class Vehicle {
    void start() { System.out.println("Vehicle starts"); }
}

class Car extends Vehicle {
    @Override
    void start() { System.out.println("Car starts with key"); }
}

Vehicle v = new Car();  // parent ref, child object
v.start();              // "Car starts with key" — runtime dispatch
```

---

# 17. Abstract Classes

### Theory:
An **abstract class** is a partially implemented class that cannot be instantiated. It serves as a common base, enforcing a contract on its subclasses.

Key rules:
- Declared with `abstract` keyword
- Can have **abstract methods** (no body — just signature) and **concrete methods** (with body)
- Any class that extends an abstract class **must implement all abstract methods**, or itself be declared abstract
- Can have constructors, fields, and static members like any regular class
- Models a concept that is incomplete on its own (e.g., a generic `Shape` without a specific geometry)

**Abstract class vs Interface**: An abstract class provides a partial implementation and can hold state; an interface defines a pure contract (more on this in section 20).

```java
abstract class Shape {
    String color;
    Shape(String c) { color = c; }

    abstract double area();          // subclass MUST implement
    void describe() {                // concrete — inherited as-is
        System.out.println(color + " shape, area=" + area());
    }
}

class Circle extends Shape {
    double r;
    Circle(String c, double r) { super(c); this.r = r; }
    @Override double area() { return Math.PI * r * r; }
}

// Shape s = new Shape("red");  // ERROR — cannot instantiate abstract
Circle c = new Circle("red", 5);
c.describe();   // red shape, area=78.53...
```

---

# 18. Polymorphism and Dynamic Method Dispatch

### Theory:
**Dynamic Method Dispatch** is the mechanism behind runtime polymorphism. When a parent-type reference calls an overridden method:
1. At **compile time**: the compiler checks that the method exists in the declared type
2. At **runtime**: the JVM looks at the actual object type and calls its version

This is the foundation of the **Open/Closed Principle** — code is open for extension (add new subclasses) but closed for modification (existing code doesn't change).

**Upcasting** (child → parent reference) is implicit and always safe.
**Downcasting** (parent reference → child type) requires explicit cast and should be guarded with `instanceof`.

```java
class Payment {
    void pay() { System.out.println("Generic payment"); }
}
class UPI  extends Payment { @Override void pay() { System.out.println("Paid via UPI"); } }
class Card extends Payment { @Override void pay() { System.out.println("Paid via Card"); } }

// Polymorphic processing
Payment[] methods = { new UPI(), new Card() };
for (Payment p : methods) p.pay();    // dispatched at runtime

// Safe downcast
Payment p = new UPI();
if (p instanceof UPI u) u.pay();      // Java 16+ pattern matching instanceof
```

---

# 19. Packages

## 19.1 Creating and Using Packages

### Theory:
A **package** is a namespace that organizes related classes and interfaces — analogous to folders in a file system.

Benefits:
- **Avoid name collisions**: `com.google.util.Date` vs `java.util.Date`
- **Access control**: default (package-private) members are invisible outside the package
- **Modularity**: group logically related types together

Naming convention: reverse domain name, all lowercase (e.g., `com.company.project.module`).

`import` brings a class into scope so you don't need its fully qualified name. `import java.util.*` imports all public types from a package (wildcard — fine for small files).

```java
// File: geometry/Circle.java
package geometry;

public class Circle {
    public double area(double r) { return Math.PI * r * r; }
}
```

```java
// File: Main.java
import geometry.Circle;

public class Main {
    public static void main(String[] args) {
        Circle c = new Circle();
        System.out.println(c.area(5));   // 78.53...
    }
}
```

## 19.2 Classpath

The **classpath** tells the JVM where to find compiled `.class` files and JARs.

```bash
javac -d out src/**/*.java          # compile, output to 'out' directory
java -cp out Main                   # run with classpath pointing to 'out'
java -cp out:lib/external.jar Main  # include a JAR on the classpath
```

---

# 20. Interfaces

## 20.1 Interface Declaration and Implementation

### Theory:
An **interface** is a pure contract — it defines *what* a class can do, not *how*. Any class that `implements` an interface must provide implementations for all its abstract methods.

Key features:
- All fields are implicitly `public static final` (constants)
- All methods are implicitly `public abstract` unless marked `default` or `static`
- **default methods** (Java 8+): concrete methods in an interface; allow backward-compatible API evolution
- **static methods** (Java 8+): utility methods on the interface itself
- A class can implement **multiple** interfaces — Java's answer to multiple inheritance
- An interface can `extend` multiple other interfaces

Interface vs Abstract Class:
| | Interface | Abstract Class |
|-|-----------|----------------|
| State (fields) | Constants only | Any |
| Constructors | None | Yes |
| Multiple inheritance | Yes | No |
| Use when | Defining a capability/role | Providing a partial template |

```java
interface Drawable { void draw(); }
interface Resizable { void resize(double factor); }

class Square implements Drawable, Resizable {
    double side;
    Square(double s) { side = s; }

    @Override public void draw()   { System.out.println("Square, side=" + side); }
    @Override public void resize(double f) { side *= f; }
}

Drawable d = new Square(4);
d.draw();                       // Square, side=4.0
```

---

# 21. Exception Handling

## 21.1 Exception Fundamentals

### Theory:
An **exception** is an event that disrupts normal program flow. Java's exception handling separates error-handling logic from normal logic, making both cleaner.

**Hierarchy**:
```
Throwable
├── Error          (JVM-level, unrecoverable — e.g., OutOfMemoryError)
└── Exception
    ├── Checked    (must be caught or declared — e.g., IOException)
    └── RuntimeException (unchecked — e.g., NullPointerException, ArrayIndexOutOfBoundsException)
```

- **Checked exceptions**: The compiler enforces handling. Forces the caller to acknowledge potential failures.
- **Unchecked exceptions**: Programming errors (bugs). Not required to catch, but can be.
- `finally` block **always executes** — ideal for releasing resources.
- `try-with-resources` (Java 7+): automatically closes `AutoCloseable` resources.

```java
try {
    int result = 10 / 0;              // ArithmeticException
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    System.out.println("Always runs");
}

// try-with-resources
try (var sc = new java.util.Scanner(System.in)) {
    System.out.println(sc.nextLine());
}  // sc closed automatically
```

---

## 21.2 Custom Exceptions

### Theory:
Custom exceptions let you model **domain-specific errors** that are meaningful to your application. They make error handling more readable and precise.

- Extend `Exception` for **checked** custom exceptions
- Extend `RuntimeException` for **unchecked** custom exceptions
- Always provide a constructor that passes a message to `super(message)`

```java
class InvalidAgeException extends Exception {
    InvalidAgeException(String msg) { super(msg); }
}

class Person {
    int age;
    void setAge(int a) throws InvalidAgeException {
        if (a < 0 || a > 150) throw new InvalidAgeException("Bad age: " + a);
        age = a;
    }
}

try { new Person().setAge(200); }
catch (InvalidAgeException e) { System.out.println(e.getMessage()); }
```

---

## 21.3 throw vs throws

| Keyword | Purpose | Where Used |
|---------|---------|------------|
| `throw` | Actually raises an exception object | Inside method body |
| `throws` | Declares that a method may raise an exception | Method signature |

`throw` is an action. `throws` is a declaration (a warning to callers).

```java
// 'throws' warns callers this method may fail
static int divide(int a, int b) throws ArithmeticException {
    if (b == 0) throw new ArithmeticException("divide by zero"); // 'throw' raises it
    return a / b;
}
```

---

# 22. String Handling

## 22.1 String Theory

**Strings in Java are immutable** — once created, a `String` object's character sequence never changes. Methods like `replace()` or `toUpperCase()` return a **new** `String` object, leaving the original intact.

- String literals are stored in the **String Pool** (a special heap area). Two literals with the same value share the same object.
- `==` compares references (addresses); `.equals()` compares content. Always use `.equals()` for string comparison.
- **StringBuilder** is a mutable alternative — much more efficient for repeated string building in loops (avoids creating many intermediate `String` objects).

### Commonly Used Methods:

| Method | Description |
|--------|-------------|
| `length()` | Number of characters |
| `charAt(i)` | Character at index |
| `substring(s, e)` | Extract portion |
| `indexOf(s)` | First occurrence index |
| `contains(s)` | Returns boolean |
| `replace(a, b)` | Replace occurrences |
| `split(regex)` | Split into array |
| `trim()` | Remove leading/trailing whitespace |
| `toUpperCase()` / `toLowerCase()` | Case conversion |
| `equals()` / `equalsIgnoreCase()` | Content comparison |

```java
String s = "Hello, World";
System.out.println(s.length());           // 12
System.out.println(s.substring(7));       // World
System.out.println(s.replace("World","Java")); // Hello, Java
System.out.println(s.contains("World")); // true

// Efficient building with StringBuilder
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 5; i++) sb.append(i).append("-");
System.out.println(sb);   // 0-1-2-3-4-
```

---

# 23. Multithreaded Programming

## 23.1 Creating Threads

### Theory:
A **thread** is the smallest unit of execution within a process. Java supports multithreading natively, allowing concurrent execution of multiple threads within the same program.

Two ways to create threads:
1. **Extend `Thread`**: Override `run()`. Simpler but limits extensibility (Java is single-inheritance).
2. **Implement `Runnable`**: Separate the task from the thread. Preferred — promotes separation of concerns and works with `ExecutorService`.

The `start()` method creates a new OS-level thread and calls `run()`. Calling `run()` directly just executes it on the current thread — **no new thread is created**.

**Thread states**: New → Runnable → Running → Blocked/Waiting → Terminated

```java
// Method 1: extend Thread
class MyThread extends Thread {
    public void run() { System.out.println("Thread: " + getName()); }
}

// Method 2: implement Runnable (preferred)
class MyTask implements Runnable {
    public void run() { System.out.println("Task running"); }
}

new MyThread().start();
new Thread(new MyTask()).start();
new Thread(() -> System.out.println("Lambda thread")).start(); // Java 8+
```

---

## 23.2 Synchronization

### Theory:
When multiple threads access **shared mutable data**, a **race condition** can occur — the result depends on thread scheduling order. `synchronized` ensures **mutual exclusion**: only one thread executes a synchronized block at a time.

- `synchronized` method: locks on `this`
- `synchronized` block: locks on a specified object (finer granularity)
- Over-synchronization leads to **deadlocks** — two threads each waiting for a lock held by the other

```java
class Counter {
    private int count = 0;
    synchronized void increment() { count++; } // thread-safe
    int getCount() { return count; }
}
```

### Key Thread Methods:

| Method | Description |
|--------|-------------|
| `start()` | Begins thread execution |
| `sleep(ms)` | Pauses current thread |
| `join()` | Waits for thread to finish |
| `isAlive()` | Checks if thread is running |
| `setPriority(n)` | Sets 1 (MIN) to 10 (MAX) |
| `setDaemon(true)` | Background thread; dies with main |

---

# 24. Java Input/Output

## 24.1 Console I/O

### Theory:
Java I/O is built on **streams** — sequences of data. `System.in` (input), `System.out` (output), and `System.err` (error) are the standard streams.

- **`Scanner`**: High-level, convenient for reading tokens from console or file
- **`BufferedReader`**: Faster for line-based reading (wraps `InputStreamReader`)
- `System.out.print` / `println` / `printf` for formatted output

```java
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
System.out.print("Enter name: ");
String name = sc.nextLine();
System.out.print("Enter age: ");
int age = sc.nextInt();
System.out.printf("Hello %s, you are %d years old.%n", name, age);
sc.close();
```

---

## 24.2 File I/O

### Theory:
Java's I/O class hierarchy:
- **Byte streams** (`InputStream`/`OutputStream`): for binary data (images, audio)
- **Character streams** (`Reader`/`Writer`): for text; handle character encoding
- Always wrap streams in **buffered** versions (`BufferedReader`, `BufferedWriter`) for performance
- Use **try-with-resources** to guarantee streams are closed even on exceptions

```java
import java.io.*;

// Writing
try (BufferedWriter bw = new BufferedWriter(new FileWriter("out.txt"))) {
    bw.write("Line 1\nLine 2");
}

// Reading
try (BufferedReader br = new BufferedReader(new FileReader("out.txt"))) {
    String line;
    while ((line = br.readLine()) != null) System.out.println(line);
}
```

---

# 25. Collection Framework

### Theory:
The **Java Collections Framework (JCF)** provides ready-made data structures and algorithms. The core interfaces are:

```
Collection
├── List     — ordered, allows duplicates
├── Set      — no duplicates
└── Queue    — FIFO ordering

Map          — key-value pairs (not part of Collection)
```

Choose the right implementation:
| Need | Use |
|------|-----|
| Fast random access | `ArrayList` |
| Fast insert/delete at ends | `LinkedList` |
| Sorted, no duplicates | `TreeSet` |
| Insertion-order set | `LinkedHashSet` |
| Fast key lookup | `HashMap` |
| Sorted keys | `TreeMap` |
| Thread-safe list | `CopyOnWriteArrayList` |
| Priority ordering | `PriorityQueue` |

---

## 25.1 List

```java
import java.util.*;

List<String> list = new ArrayList<>(List.of("Banana", "Apple"));
list.add("Cherry");
list.sort(null);                        // natural order
System.out.println(list);              // [Apple, Banana, Cherry]
System.out.println(list.get(0));       // Apple
list.remove("Banana");
System.out.println(list.size());       // 2
```

---

## 25.2 Set

```java
Set<Integer> set = new HashSet<>(Arrays.asList(3, 1, 2, 1, 3));
System.out.println(set);          // {1, 2, 3} — duplicates gone, unordered

Set<Integer> sorted = new TreeSet<>(set);
System.out.println(sorted);       // [1, 2, 3] — sorted
```

---

## 25.3 Map

```java
Map<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);
scores.put("Bob", 82);
scores.put("Alice", 99);          // overwrites
System.out.println(scores.get("Alice"));    // 99
scores.forEach((k, v) -> System.out.println(k + "=" + v));
```

---

## 25.4 Queue and Deque

```java
Queue<Integer> queue = new LinkedList<>(List.of(1, 2, 3));
System.out.println(queue.peek());  // 1 (front, no remove)
System.out.println(queue.poll());  // 1 (remove front)
System.out.println(queue);         // [2, 3]

PriorityQueue<Integer> pq = new PriorityQueue<>(List.of(30, 10, 20));
while (!pq.isEmpty()) System.out.print(pq.poll() + " "); // 10 20 30
```

---

# Quick Reference Summary

## OOP Pillars

| Pillar | Keyword(s) | Core Idea |
|--------|-----------|-----------|
| **Encapsulation** | `private`, getters/setters | Hide state, expose behavior |
| **Inheritance** | `extends`, `super` | Reuse and extend existing classes |
| **Polymorphism** | `@Override`, dynamic dispatch | One interface, many forms |
| **Abstraction** | `abstract`, `interface` | Hide complexity, expose contracts |

## Access Modifiers (most → least restrictive)
`private` → *(default)* → `protected` → `public`

## Key Keywords

| Keyword | Meaning |
|---------|---------|
| `static` | Belongs to class, not instance |
| `final` | Cannot change (variable), extend (class), or override (method) |
| `abstract` | Incomplete — must be implemented by subclass |
| `super` | Refers to parent class |
| `this` | Refers to current object |
| `instanceof` | Runtime type check |
| `synchronized` | Thread-safe critical section |

## Exception Hierarchy
```
Throwable
├── Error                   (don't catch — JVM issues)
└── Exception
    ├── RuntimeException    (unchecked — programming bugs)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   └── ArithmeticException
    └── Checked             (must handle)
        ├── IOException
        └── FileNotFoundException
```

## Collections Cheat Sheet

| Interface | Common Impl | Ordered? | Duplicates? | Null? |
|-----------|------------|---------|-------------|-------|
| `List` | `ArrayList`, `LinkedList` | Yes (index) | Yes | Yes |
| `Set` | `HashSet`, `TreeSet` | No / sorted | No | One null (Hash) |
| `Map` | `HashMap`, `TreeMap` | No / sorted keys | Keys: No | One null key (Hash) |
| `Queue` | `LinkedList`, `PriorityQueue` | FIFO / priority | Yes | Depends |

---

*Master the concepts, not just the syntax — Java OOP is about modeling the real world in a maintainable, extensible way.*