from db_connection import DatabaseConnection

def main():
    db = DatabaseConnection()
    db.connect()
    results = db.execute_query('SELECT * FROM users')
    db.close()
    print(results)


if __name__ == "__main__":
    main()