import sqlite3
from singleton import Singleton


@Singleton
class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = self.create_connection()
        self.cursor = self.create_cursor()

    def __str__(self):
        return "Database connection object"

    def create_connection(self):
        conn = sqlite3.connect(self.database_name)
        return conn

    def create_cursor(self):
        cur = self.connection.cursor()
        return cur

    def execute_sql(self, sql):
        self.cursor.execute(sql)
