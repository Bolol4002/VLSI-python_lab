public class exp7 {
    static class Equate {
        int area(int a, int b) {
            return a*b;
        }
        double area(int r) {
            return (3.14)*r*r;
        }
    }
    public static void main(String[] args) {
        Equate calc = new Equate();
        System.out.println(calc.area(100, 34));
        System.out.println(calc.area(500));
    }
}
