public class Exp05ClassesObjectsMethods {
    static class Box {
        int length;

        Box(int length) {
            this.length = length;
        }

        int doubleLength() {
            return length * 2;
        }
    }

    public static void main(String[] args) {
        Box b = new Box(5);
        System.out.println(b.doubleLength());
    }
}
