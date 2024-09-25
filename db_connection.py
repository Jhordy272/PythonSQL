# db_connection.py
import pymysql
import os

class DatabaseConnection:
    def __init__(self):
        self.host = os.environ.get('DB_HOST')
        self.user = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')
        self.db = os.environ.get('DB_DB')
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f'Error connecting: {e}')

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f'Error executing query: {e}')
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()