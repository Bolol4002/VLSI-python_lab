public class Exp07MethodOverloading {
    static class Calculator {
        int area(int a, int b) {
            return a*b;
        }

        double area(int r) {
            return (3.14)*r*r;
        }
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.area(2, 3));
        System.out.println(calc.area(7));
    }
}
