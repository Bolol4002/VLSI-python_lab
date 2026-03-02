class exp12 {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Order");

        sb.append(" Created");
        System.out.println("Append: " + sb);

        sb.insert(5, " #102");
        System.out.println("Insert: " + sb);

        sb.replace(6, 10, "205");
        System.out.println("Replace: " + sb);

        sb.delete(6, 9);
        System.out.println("Delete: " + sb);

        sb.reverse();
        System.out.println("Reverse: " + sb);

        System.out.println("Length: " + sb.length());
    }
}