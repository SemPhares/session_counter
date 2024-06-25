from sqlalchemy import  Column,  String, Integer
from database import Base


class Count_model(Base):
    __tablename__ = "counts"
    id = Column(String, primary_key=True)
    user_first_name = Column(String)
    user_last_name = Column(String)
    num_count = Column(String)
    nom_salle = Column(String)
    zone_count = Column(String)
    genre_count = Column(String)
    date = Column(String)
    time = Column(String)
    count = Column(Integer)

