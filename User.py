from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Rol import Rol

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    id_rol = Column(Integer, ForeignKey(Rol.id))  

    rol = relationship(Rol)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, rol={self.rol})>"