from SqlHandler import SqlHandler


class Employee:
    employees = []
    table = 'employees'
    db = SqlHandler(host="localhost", user="root",
                    password="", database="pythondb")

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.id = None
        self.data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary,
        }
        Employee.employees.append(self)
        self.id = Employee.db.insert_to_database(Employee.table, self.data)

    def transfer(self, new_department):
        self.department = new_department
        Employee.db.update_database(self.id, new_department)

    @staticmethod
    def fire(employee_id):
        employee = Employee.get_employee_by_id(employee_id)
        if employee:
            Employee.employees.remove(employee)
            Employee.db.delete_from_database(Employee.table, employee_id)
        else:
            print("Employee with ID {} not found.".format(employee_id))

    @staticmethod
    def get_employee_by_id(id):
        for employee in Employee.employees:
            if employee.id == id:
                return employee
        return None

    @classmethod
    def show_all_employees(cls):
        employees = cls.db.get_all_data('employees')
        cls.print_employees(employees)

    def print_employees(rows):
        print("{:<5} {:<15} {:<15} {:<5} {:<15} {:<10}".format(
            "ID", "First Name", "Last Name", "Age", "Department", "Salary"))
        print("-" * 70)
        for row in rows:
            print("{:<5} {:<15} {:<15} {:<5} {:<15} {:<10}".format(
                row[0], row[1], row[2], row[3], row[4], row[5]))

    @classmethod
    def print_employees_list(cls):
        print("ID\tFirst Name\tLast Name\tAge\tDepartment\tSalary")
        for employee in cls.employees:
            print("{}\t{}\t\t{}\t\t{}\t{}\t\t{}".format(employee.id, employee.first_name,
                  employee.last_name, employee.age, employee.department, employee.salary))