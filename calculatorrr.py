import mysql
from mysql.connector import Error


class Database:
    @staticmethod
    def connect_to_db():
        try:
            print('yupp')
            return mysql.connector.connect(
                host='localhost',
                user='yashi',
                password='Password@123',
                database='USER', auth_plugin='mysql_native_password'
            )
        except Error as e:
            print("Error connecting to MySQL: ", e)
            return None

    @staticmethod
    def create_table(connection):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Calculations (
            operation VARCHAR(10),
            result FLOAT
        )
        """
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()

    @staticmethod
    def insert_calculation(connection, operation, result):
        insert_query = """
        INSERT INTO Calculations (operation, result)
        VALUES (%s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(insert_query, (operation, result))
        connection.commit()
class Calculator:
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def sub(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def mul(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def div(x: float, y: float) -> float:
        if y == 0:
            raise ZeroDivisionError("Zero cannot be divided")
        return x / y

    @staticmethod
    def perform_calculations():
        connection = Database.connect_to_db()
        if connection is not None:
            Database.create_table(connection)
            calculations = [
                ("Add", Calculator.add(2, 48)),
                ("Subtract", Calculator.sub(4, 2)),
                ("Multiply", Calculator.mul(2, 46)),
                ("Divide", Calculator.div(4, 5))
            ]
            for operation, result in calculations:
                Database.insert_calculation(connection, operation, result)
                print("The result of", operation, "operation:", result)
            connection.close()
        else:
            print("Failed to connect to the database")


Calculator.perform_calculations()