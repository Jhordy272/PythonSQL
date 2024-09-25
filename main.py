from db_connection import DatabaseConnection
from db_connection_ORM import DatabaseConnectionORM
from User import User

def main():
    db = DatabaseConnection()
    db.connect()
    results = db.execute_query('SELECT u.id, u.username, u.password, u.email, r.name FROM api_test_report.users u JOIN api_test_report.rol r ON u.id_rol = r.id')
    db.close()
    print(results)

def main_ORM():
    db = DatabaseConnectionORM()
    Base = db.get_base()
    engine = db.get_engine()
    Base.metadata.create_all(engine)
    session = db.get_session()
    users = session.query(User).all()
    print(users)
    db.close()

if __name__ == "__main__":
    main()
    main_ORM()