from SqlHandler import SqlHandler


def create_table_employees():
    db = SqlHandler(host="localhost", user="root",
                    password="", database="pythondb")
    db.connect()
    table_name = "employees2"
    columns = [
        "id INT AUTO_INCREMENT PRIMARY KEY",
        "first_name VARCHAR(255) NOT NULL",
        "last_name VARCHAR(255) NOT NULL",
        "age INT",
        "department VARCHAR(255)",
        "salary INT"
    ]
    db.create_table(table_name, columns)
    db.close()


def create_table_managers():
    db = SqlHandler(host="localhost", user="root",
                    password="mypassword", database="mydatabase")
    db.connect()
    table_name = "managers"
    columns = [
        "id INT AUTO_INCREMENT PRIMARY KEY",
        "first_name VARCHAR(255) NOT NULL",
        "last_name VARCHAR(255) NOT NULL",
        "age INT",
        "department VARCHAR(255)",
        "salary INT"
        "managed_department VARCHAR(255)"
    ]
    db.create_table(table_name, columns)
    db.close()


create_table_employees()
create_table_managers()