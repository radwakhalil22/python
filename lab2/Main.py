from SqlHandler import SqlHandler
from Employee import Employee
from Manager import Manager


def print_menu():
    print("Menu:")
    print("a - Add new employee")
    print("b - remove employee")
    print("c - show employees")
    print("q - Quit")


def print_second_menu():
    print("Menu:")
    print("e - employee ?")
    print("m - Manager ?")
    print("q - Quit")


def add_employee():
    print("Add new employee:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    salary = int(input("Salary: "))
    employee = Employee(first_name=first_name, last_name=last_name,
                        age=age, department=department, salary=salary)
    Employee.print_employees_list()
    print("Employee added successfully.")


def add_manager():
    print("Add new manager:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    salary = int(input("Salary: "))
    managed_department = input("managed department: ")
    manager = Manager(first_name=first_name, last_name=last_name,
                      age=age, department=department, salary=salary, managed_department=managed_department)

    print("Manager added successfully.")


def fire_employee():
    print("fire employee:")
    employee_id = input("id: ")
    Employee.fire(int(employee_id))
    print("Employee deleted successfully.")


def fire_manager():
    print("fire manager:")
    manager_id = input("id: ")
    Manager.fire(manager_id)
    print("Manager deleted successfully.")


def show_all_employees():
    print("show all employees:")
    Employee.show_all_employees()


def show_all_managers():
    print("show all managers:")
    Manager.show_all_managers()


def main():
    db = SqlHandler(host="localhost", user="root",
                    password="", database="pythondb")
    print("Welcome to the Employee Management System.")
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "a":
            print_second_menu()
            choice = input("Enter your choice: ")
            if choice == "e":
                add_employee()
            if choice == "m":
                add_manager()
        elif choice == "b":
            print_second_menu()
            choice = input("Enter your choice: ")
            if choice == "e":
                fire_employee()
            if choice == "m":
                fire_manager()
        elif choice == "c":
            print_second_menu()
            choice = input("Enter your choice: ")
            if choice == "e":
                show_all_employees()
            if choice == "m":
                show_all_managers()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()