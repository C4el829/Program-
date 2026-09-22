package Lab12;

class Keyboard {
    private String type;

    public Keyboard(String type) {
        this.type = type;
    }

    public String getKey() {
        return type;
    }
}

class Printer {
    public void print() {
        System.out.println("Shared printer is printing...");
    }
}

class Computer {
    private Keyboard keyboard;

    public Computer(Keyboard keyboard) { // Composition
        this.keyboard = keyboard;
    }

    public void start() {
        System.out.println("Computer started with keyboard: " + keyboard.getKey());
    }

    public void printDocument(Printer printer) { // Aggregation
        printer.print();
    }
}

public class Main4 {
    public static void main(String[] args) {
        Printer sharedPrinter = new Printer();

        Computer pc1 = new Computer(new Keyboard("Mechanical"));
        Computer pc2 = new Computer(new Keyboard("Wireless"));

        pc1.start();
        pc2.start();

        pc1.printDocument(sharedPrinter);
        pc2.printDocument(sharedPrinter);
    }
}