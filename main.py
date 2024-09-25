import pymysql
import os

HOST = os.environ.get('DB_HOST')
USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
DB = os.environ.get('DB_DB')

connection = pymysql.connect(host=HOST,user=USER,password=PASSWORD,db=DB)

cursor = connection.cursor()

cursor.execute('SELECT * FROM users')

for row in cursor:
    print(row)

connection.close()