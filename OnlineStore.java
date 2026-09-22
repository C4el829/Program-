package Lab12;

class Product {
    String name;
    double price;

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }
}

class OrderItem {
    Product product;
    int quantity;

    public OrderItem(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    public double getTotal() {
        return product.price * quantity;
    }
}

class Order {
    private OrderItem[] items;

    public Order(OrderItem[] items) {
        this.items = items;
    }

    public double calculateTotal() {
        double total = 0;
        for (OrderItem item : items) {
            total += item.getTotal();
        }
        return total;
    }
}

class Customer {
    String name;

    public Customer(String name) {
        this.name = name;
    }

    public void placeOrder(Order order) {
        System.out.println(name + "'s total order amount: " + order.calculateTotal());
    }
}

public class OnlineStore {
    public static void main(String[] args) {
        Product p1 = new Product("Laptop", 2500);
        Product p2 = new Product("Mouse", 50);

        OrderItem item1 = new OrderItem(p1, 1);
        OrderItem item2 = new OrderItem(p2, 2);

        Order order = new Order(new OrderItem[]{item1, item2});

        Customer customer = new Customer("Anu");
        customer.placeOrder(order);
    }
}