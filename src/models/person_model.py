from sqlalchemy import  Column,  String
from database import Base


class Person_model(Base):
    __tablename__ = "persons"
    id = Column(String, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
