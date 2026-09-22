import json
import os   

class Employee_Management_System:
    def __init__(self, filename='employees.json'):
        self.filename = filename
        self.employees = self.load_data()

    def load_data(self):
        """Loads data from the file. If file doesn't exist, returns empty dict."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        """Saves the current employee dictionary to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.employees, file, indent=4)
        print("Data successfully saved to file.")

    def add_employee(self, emp_id, name, position, salary):
        """Adds or updates an employee and saves immediately."""
        emp_id = emp_id.strip()
        self.employees[emp_id] = {
            "name": name,
            "position": position,
            "salary": salary,
        }
        self.save_data()
        print(f"Employee {name} added.")

    def search_employee(self, emp_id):
        """Searches for an employee by their ID."""
        emp_id = emp_id.strip()
        emp = self.employees.get(emp_id)
        if emp:
            print(f"\n--- Record Found ---")
            print(f"ID: {emp_id}\nName: {emp['name']}\nPosition: {emp['position']}\nSalary: {emp['salary']}")
        else:
            print(f"No employee found with ID: {emp_id}")
    def delete_employee(self, emp_id):
        """Deletes an employee by ID."""
        emp_id = emp_id.strip()
        if emp_id in self.employees:
            deleted_name = self.employees[emp_id]['name']
            del self.employees[emp_id]
            self.save_data()
            print(f"Employee {deleted_name} deleted successfully.")
        else:
            print("Employee not found.")
    
    def view_all_employees(self):
        """Displays all employees in a formatted table."""
        if not self.employees:
            print("\nNo employees in the system.")
            return
        
        print("\n" + "="*80)
        print(f"{'ID':<10} {'Name':<20} {'Position':<25} {'Salary':<15}")
        print("="*80)
        
        for emp_id, emp_info in self.employees.items():
            print(f"{emp_id:<10} {emp_info['name']:<20} {emp_info['position']:<25} {emp_info['salary']:<15}")
        
        print("="*80)
        print(f"Total Employees: {len(self.employees)}")
    
    def change_employee_position(self, emp_id, new_position):
        """Changes an employee's position by ID."""
        emp_id = emp_id.strip()
        if emp_id in self.employees:
            old_position = self.employees[emp_id]['position']
            self.employees[emp_id]['position'] = new_position
            self.save_data()
            print(f"Position updated for {self.employees[emp_id]['name']}: {old_position} -> {new_position}")
        else:
            print(f"No employee found with ID: {emp_id}")
    
    def change_employee_salary(self, emp_id, new_salary):
        """Changes an employee's salary by ID."""
        emp_id = emp_id.strip()
        if emp_id in self.employees:
            old_salary = self.employees[emp_id]['salary']
            self.employees[emp_id]['salary'] = new_salary 
            self.save_data()
            print(f"Salary updated for {self.employees[emp_id]['name']}: {old_salary} -> {new_salary}")
        else:
            print(f"No employee found with ID: {emp_id}")
    
    def change_employee_name(self, emp_id, new_name):
        """Changes an employee's name by ID."""
        emp_id = emp_id.strip()
        if emp_id in self.employees:
            old_name = self.employees[emp_id] ['name']
            self.employees[emp_id]['name'] = new_name
            self.save_data()
            print(f"Name updated for ID {emp_id}: {old_name} -> {new_name}")
        else:
            print(f"No employee found with ID: {emp_id}")

# --- Simple Menu Interface ---
def main():
    system = Employee_Management_System()
    
    while True:
        print("\n1. Add Employee\n2. Search Employee\n3. View All Employees\n4. Change Employee Position\n5. Change Employee Salary\n6. Change Employee Name\n7. Delete Employee\n8. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            eid = input("Enter ID: ")
            name = input("Enter Name: ")
            pos = input("Enter Position: ")
            sal = input("Enter Salary: ")
            system.add_employee(eid, name, pos, sal)
        
        elif choice == '2':
            eid = input("Enter ID to search: ")
            system.search_employee(eid)

        elif choice == '3':
            system.view_all_employees()

        elif choice == '4':
            eid = input("Enter ID to change position: ")
            new_pos = input("Enter new position: ")
            system.change_employee_position(eid, new_pos)

        elif choice == '5':
            eid = input("Enter ID to change salary: ")
            new_sal = input("Enter new salary: ")
            system.change_employee_salary(eid, new_sal)

        elif choice == '6':
            eid = input("Enter ID to change name: ")
            new_name = input("Enter new name: ")
            system.change_employee_name(eid, new_name) 
        
        elif choice == '7':
            eid = input("Enter ID to delete: ")
            system.delete_employee(eid)

        elif choice == '8':
            print("Goodbye!")
            break
        
        else:
            print("Invalid selection.")

if __name__ == "__main__":  
    main()