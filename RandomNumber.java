package Lab11;
import java.util.Random;

public class RandomNumber {
    public static void main(String[] args) {
        Random rand = new Random();
        int num = rand.nextInt(100) + 1;

        System.out.println("Random Number: " + num);
    }
}