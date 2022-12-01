import sqlite3

from query import table_list

class DatabaseConnection:
    def __init__(self, db_file:str = "stock.db"):
        self.db_file = db_file
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    def create_connection(self):
        try:
            connection = sqlite3.connect(self.db_file)
            return connection
        except ValueError as e:
            print(e)
        
    def create_table(self, sql_table):
        try:
            self.cursor.execute(sql_table)
            self.connection.commit()
        except ValueError as e:
            print(e)
    
    def execute_query(self, data):
        try:
            print(f"Writing {data}")
            self.cursor.execute("INSERT INTO stock VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
            self.connection.commit()
        except ValueError as e:
            print(e)
    
    def list_all_stocks(self):
        try:
            self.cursor.execute("SELECT * FROM stock")
            rows = self.cursor.fetchall()
            return rows
        except ValueError as e:
            print(e)
    
    def close_connection(self):
        self.connection.close()

if __name__ == '__main__':
    obj = DatabaseConnection()
    for query in table_list: 
        obj.create_table(query)