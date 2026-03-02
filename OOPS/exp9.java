interface Delivery {
    void deliver(int items);
}

interface Tracker {
    void track(String msg);
}

interface Reporter {
    void report(String info);
}

class BasicDelivery implements Delivery {
    public void deliver(int items) {
        System.out.println("Items delivered: " + items);
    }
}

class AdvancedDelivery implements Delivery, Tracker, Reporter {

    public void deliver(int items) {
        System.out.println("Priority items delivered: " + items);
    }

    public void track(String msg) {
        System.out.println("Tracking: " + msg);
    }

    public void report(String info) {
        System.out.println("Report: " + info);
    }
}

public class exp9 {
    public static void main(String[] args) {

        BasicDelivery basic = new BasicDelivery();
        basic.deliver(2);

        System.out.println("-----");

        AdvancedDelivery adv = new AdvancedDelivery();
        adv.deliver(4);
        adv.track("Parcel reached hub");
        adv.report("Shipment logged");
    }
}