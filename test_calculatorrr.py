import unittest
import mysql.connector
from unittest.mock import MagicMock, patch
from calculatorrr import Calculator


class TestCalculator(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_connect_to_db_success(self, mock_connect):
        mock_connection = MagicMock(spec=mysql.connector.MySQLConnection)
        mock_connect.return_value = mock_connection
        connection = Calculator.connect_to_db()

        self.assertIsNotNone(connection)

        mock_connect.assert_called_once_with(
            host='localhost',
            user='root',
            password='Yashi22@sql',
            database='USER'
        )

    @patch('mysql.connector.connect')
    def test_connect_to_db_failure(self, mock_connect):
        mock_connect.side_effect = mysql.connector.Error("Connection failed")
        connection = Calculator.connect_to_db()
        self.assertIsNone(connection)

    @patch.object(Calculator, 'connect_to_db')
    def test_create_table(self, mock_connect_to_db):
        mock_connection = MagicMock(spec=mysql.connector.MySQLConnection)
        mock_connect_to_db.return_value = mock_connection

        Calculator.create_table(mock_connection)

        mock_connection.cursor.return_value.execute.assert_called_once_with("""
        CREATE TABLE IF NOT EXISTS Calculations (
            operation VARCHAR(10),
            result FLOAT
        )
        """)

    def test_add(self):
        result = Calculator.add(4, 2)
        self.assertEqual(result, 6)

    def test_sub(self):
        result = Calculator.sub(4, 2)
        self.assertEqual(result, 2)

    def test_mul(self):
        result = Calculator.mul(4, 2)
        self.assertEqual(result, 8)

    def test_div(self):
        result = Calculator.div(4, 2)
        self.assertEqual(result, 2)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.div(4, 0)


if __name__ == '__main__':
    unittest.main()