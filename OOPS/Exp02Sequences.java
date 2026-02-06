public class Exp02Sequences {
    public static void main(String[] args) {
        int n = 6;
        int a = 0, b = 1;

        for (int i = 0; i < n; i++) {
            System.out.print(a + (i == n - 1 ? "" : " "));
            int next = a + b;
            a = b;
            b = next;
        }
        System.out.println();
    }
}
