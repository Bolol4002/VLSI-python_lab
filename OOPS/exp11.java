class exp11 {

    static void checkBalance(int amount) throws Exception {
        if (amount < 500) {
            throw new Exception("Minimum balance not maintained.");
        } else {
            System.out.println("Transaction approved.");
        }
    }

    public static void main(String[] args) {

        try {
            checkBalance(300);
        }
        catch (Exception e) {
            System.out.println("Exception caught: " + e.getMessage());
        }
        finally {
            System.out.println("Finally block always executes.");
        }
    }
}