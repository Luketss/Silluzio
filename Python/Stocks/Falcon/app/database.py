import sqlite3

from query import table_list


class DatabaseConnection:
    def __init__(self, connection_string: str = "stock.db"):
        self.connection_string = connection_string
        self._connection = self._create_connection()
        self._cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _create_connection(self):
        try:
            connection = sqlite3.connect(self.connection_string)
            return connection
        except ValueError as e:
            print(e)

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def create_table(self, sql_table):
        try:
            self.cursor.execute(sql_table)
            self.connection.commit()
        except ValueError as e:
            print(e)

    # def execute_query(self, data):
    #     try:
    #         print(f"Writing {data}")
    #         self.cursor.execute(
    #             "INSERT INTO stock VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data
    #         )
    #         self.connection.commit()
    #     except ValueError as e:
    #         print(e)

    def list_all_stocks(self):
        sql = "SELECT * FROM stock"
        return self.query(sql)

    def stock_by_date(self, field, value):
        sql = "SELECT * FROM stock WHERE ? = ?"
        return self.query(
            sql,
            (
                field,
                value,
            ),
        )


if __name__ == "__main__":
    obj = DatabaseConnection()
    for query in table_list:
        obj.create_table(query)
