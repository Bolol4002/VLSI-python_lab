import java.util.*;

class exp13 {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Bus101");
        list.add("Train220");
        list.add("Flight330");
        list.add("Train220");

        System.out.println("ArrayList:");
        System.out.println(list);
        System.out.println("Allows duplicates & maintains insertion order\n");

        Set<String> hashSet = new HashSet<>();
        hashSet.add("Bus101");
        hashSet.add("Train220");
        hashSet.add("Flight330");
        hashSet.add("Train220");

        System.out.println("HashSet:");
        System.out.println(hashSet);
        System.out.println("No duplicates & no guaranteed order\n");

        Set<String> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add("Bus101");
        linkedHashSet.add("Train220");
        linkedHashSet.add("Flight330");
        linkedHashSet.add("Train220");

        System.out.println("LinkedHashSet:");
        System.out.println(linkedHashSet);
        System.out.println("No duplicates & maintains insertion order\n");

        Set<String> treeSet = new TreeSet<>();
        treeSet.add("Bus101");
        treeSet.add("Train220");
        treeSet.add("Flight330");
        treeSet.add("Train220");

        System.out.println("TreeSet:");
        System.out.println(treeSet);
        System.out.println("No duplicates & sorted order\n");

        long start = System.nanoTime();
        for(int i=0; i<100000; i++){
            list.add("Trip" + i);
        }
        long end = System.nanoTime();
        System.out.println("ArrayList insertion time: " + (end - start) + " ns");

        start = System.nanoTime();
        for(int i=0; i<100000; i++){
            hashSet.add("Trip" + i);
        }
        end = System.nanoTime();
        System.out.println("HashSet insertion time: " + (end - start) + " ns");
    }
}