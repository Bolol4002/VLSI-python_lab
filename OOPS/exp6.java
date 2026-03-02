public class exp6 {
    static class Student {
        String name;

        Student() {
            this("Hello");
        }

        Student(String name) {
            this.name = name;
        }
    }
    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student("Bye bye");
        System.out.println(s1.name);
        System.out.println(s2.name);
    }
}
