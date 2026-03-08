import mypackage.BillCalculator;
public class exp10 {
    public static void main(String[] args) {

        BillCalculator b = new BillCalculator();
        int units = 120;
        int ratePerUnit = 6;
        System.out.println("Electricity Bill = " + b.calculate(units, ratePerUnit));
    }
}
