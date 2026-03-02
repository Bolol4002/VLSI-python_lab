import mypackage.Calculator;
public class exp10 {
    public static void main(String[] args) {

        Calculator c = new Calculator();
        int baseFare = 120;
        int serviceCharge = 30;
        System.out.println("Total Fare = " + c.add(baseFare, serviceCharge));
    }
}
