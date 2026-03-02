class Vehicle {
    void move() {
        System.out.println("Vehicle is moving");
    }
}

class Car extends Vehicle {
    void display() {
        System.out.println("Car is a vehicle");
    }
}

public class exp8 {
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.move();
        myCar.display();
    }
}
