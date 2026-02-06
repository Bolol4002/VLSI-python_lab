public class Exp01DecisionLoops {
    public static void main(String[] args) {
        int n = 7;

        if (n % 2 == 0) {
            System.out.println("even");
        } else {
            System.out.println("odd");
        }

        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        System.out.println("sum=" + sum);
    }
}
