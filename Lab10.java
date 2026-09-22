package Lab10;

import java.util.Scanner; // Гараас утга уншихад заавал импортлоно

class Student {
    private String id;
    private String name;
    private double gpa;
    private int birthYear;

    public Student(String id, String name, double gpa, int birthYear) {
        this.id = id;
        this.name = name;
        this.gpa = gpa;
        this.birthYear = birthYear;
    }

    public void printInfo() {
        System.out.println("\n--- Student Information ---");
        System.out.println("ID: " + id + " | Name: " + toUpperName() + 
                           " | GPA: " + gpa + " | Age: " + getAge(2026));
    }

    public int getAge(int currentYear) {
        return currentYear - birthYear;
    }

    public String toUpperName() {
        return name.toUpperCase();
    }
}

public class Lab10 {
    public static void main(String[] args) {
        // Scanner объект үүсгэх 
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter student information.");

        System.out.print("ID: ");
        String id = input.nextLine(); // Текст унших 

        System.out.print("Name: ");
        String name = input.nextLine();

        System.out.print("GPA: ");
        double gpa = input.nextDouble(); // Бутархай тоо унших

        System.out.print("Birth Year: ");
        int year = input.nextInt(); // Бүхэл тоо унших 

        // Гараас авсан утгуудаар объект үүсгэх
        Student s = new Student(id, name, gpa, year);
        
        // Үр дүнг хэвлэх
        s.printInfo();
        
        input.close(); // Scanner-ийг хаах 
    }
}