from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rol(Base):
    __tablename__ = 'rol'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)

    def __repr__(self):
        return f"<Rol(id={self.id}, name={self.name})>"