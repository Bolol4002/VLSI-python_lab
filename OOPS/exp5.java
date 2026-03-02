public class exp5 {
    static class square {
        int length;

        square(int length) {
            this.length = length;
        }

        int doubleLength() {
            return length * 2;
        }
    }

    public static void main(String[] args) {
        square b = new square(5);
        System.out.println(b.doubleLength());
    }
}
