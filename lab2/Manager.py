from Employee import Employee


class Manager(Employee):
    table = 'managers'

    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.id = None
        self.managed_department = managed_department
        self.data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary,
            "managed_department": self.managed_department
        }
        self.id = Manager.db.insert_to_database(Manager.table, self.data)

    def print_manager(self):
        print("{:<5} {:<15} {:<15} {:<5} {:<15} {:<10} {:<15}".format(
            self.id, self.first_name, self.last_name, self.age, self.department, 'Secret Data', self.managed_department))

    @staticmethod
    def fire(id):
        Manager.db.delete_from_database(Manager.table, id)

    @classmethod
    def show_all_managers(cls):
        managers = cls.db.get_all_data("managers")
        cls.print_managers(managers)

    def print_managers(rows):
        print("{:<5} {:<15} {:<15} {:<5} {:<15} {:<10} {:<15}".format(
            "ID", "First Name", "Last Name", "Age", "Department", "Salary", "Managed Department"))
        print("-" * 95)
        for row in rows:
            manager = Manager(*row[1:6], row[6])
            manager.id = row[0]
            manager.print_manager()