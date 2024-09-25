from db_connection import DatabaseConnection

def main():
    db = DatabaseConnection()
    db.connect()
    results = db.execute_query('SELECT u.id, u.username, u.password, u.email, r.name FROM api_test_report.users u JOIN api_test_report.rol r ON u.id_rol = r.id')
    db.close()
    print(results)


if __name__ == "__main__":
    main()