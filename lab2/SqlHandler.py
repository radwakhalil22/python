import mysql.connector


class SqlHandler():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database")
            return self.connection
        except mysql.connector.Error as e:
            raise Exception("Error connecting to MySQL database: {}".format(e))

    def get_all_data(self, table):
        try:
            self.connect()
            query = 'SELECT * FROM {}'.format(table)
            rows = self.execute_query(query)
            self.close()
            return rows
        except mysql.connector.Error as e:
            raise Exception("Error connecting to MySQL database: {}".format(e))

    def delete_from_database(self, table, record_id):
        try:
            self.connect()
            query = "DELETE FROM {} WHERE id = %s".format(table)
            params = (record_id,)
            self.execute_query(query, params)
        except mysql.connector.Error as e:
            raise Exception("Error deleting record: {}".format(e))
        finally:
            self.close()

    def insert_to_database(self, table, data):
        try:
            self.connect()
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = 'INSERT INTO {} ({}) VALUES ({})'.format(
                table, columns, placeholders)
            params = tuple(data.values())
            self.execute_query(query, params)
            id = self.cursor.lastrowid
            return id
        except mysql.connector.Error as e:
            raise Exception("Error connecting to MySQL database: {}".format(e))

    def update_database(self, emp_id, new_department):
        try:
            self.connect()
            query = '''UPDATE employees
                    SET department = %s
                    WHERE id = %s'''

            params = (new_department, emp_id)
            self.execute_query(query, params)
        except mysql.connector.Error as e:
            raise Exception("Error connecting to MySQL database: {}".format(e))

    def create_table(self, table_name, columns):
        try:
            columns_str = ", ".join(columns)
            query = f"CREATE TABLE {table_name} ({columns_str})"
            self.cursor.execute(query)

        except mysql.connector.Error as e:
            print(e)

    def execute_query(self, query, params=None):
        try:
            conn = self.connect()
            self.cursor.execute(query, params)
            results = self.cursor.fetchall()
            conn.commit()
            self.close()
            return results
        except mysql.connector.Error as e:
            print(e)

    def close(self):
        self.cursor.close()
        self.connection.close()