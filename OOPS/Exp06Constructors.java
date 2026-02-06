public class Exp06Constructors {
    static class Student {
        String name;

        Student() {
            this("Unknown");
        }

        Student(String name) {
            this.name = name;
        }
    }

    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student("Alice");
        System.out.println(s1.name);
        System.out.println(s2.name);
    }
}
