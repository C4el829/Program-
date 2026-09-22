package Lab9;

import java.util.Scanner; // Гараас утга авахад заавал импортлох шаардлагатай 

public class Task3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Scanner объект үүсгэх 
        
        System.out.print("Нэрээ оруулна уу: ");
        String name = input.nextLine(); // Нэр унших
        
        System.out.print("Насаа оруулна уу: ");
        int age = input.nextInt(); // Нас унших 
        
        System.out.println("Сайн уу, " + name + "!"); // Мэндчилгээ 
        System.out.println("Ирэх жил чи " + (age + 1) + " настай болно."); // Насан дээр 1-ийг нэмж хэвлэх 
        
        input.close(); // Scanner-ийг хаах 
    }
}
