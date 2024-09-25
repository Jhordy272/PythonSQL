from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

class DatabaseConnectionORM:
    def __init__(self):
        self.host = os.environ.get('DB_HOST')
        self.user = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')
        self.db = os.environ.get('DB_DB')
        try:
            self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.db}')
        except Exception as e:
            print(f'Error connecting: {e}')

    def get_base(self):
        return declarative_base()
    
    def get_engine(self):
        return self.engine

    def get_session(self): 
        Session = sessionmaker(bind=self.engine)
        return Session()
    
    def close(self):
        self.engine.dispose()