import uuid
import datetime
from typing import List
from sqlalchemy.orm import Session
from schemas.person_schema import Person
from models.count_model import Count_model
from schemas.count_shcema import Count, Count_form



def get_count_by_id(db: Session, id: str):
    return db.query(Count_model).filter(Count_model.id == id).first()

def write_count_to_database(db: Session,
                            current_user: Person,
                            count_form: Count_form,
                            count: int) -> Count:
    counting_id = str(uuid.uuid4())
    db_count = Count_model(
        id= counting_id,
        user_first_name = current_user.first_name,
        user_last_name = current_user.last_name,
        num_count = count_form.num_count,
        nom_salle = count_form.nom_salle,
        zone_count = count_form.zone_count,
        genre_count = count_form.genre_count,
        date = datetime.datetime.now().strftime("%d/%m/%y"),
        time = datetime.datetime.now().strftime("%H:%M:%S"),
        count = count)
    db.add(db_count)
    db.commit()

    count_ = Count(id = counting_id, genre_count = count_form.genre_count, count = count)
    return count_

def get_all_counts(db: Session) -> List[Count_model]:
    return db.query(Count_model).all()

def get_count_by_genre(db: Session, genre: str) -> List[Count_model]:
    return db.query(Count_model).filter(Count_model.genre_count == genre).all()

def count_by_user(db: Session, user: Person) -> List[Count_model]:
    return db.query(Count_model).filter(
        Count_model.user_first_name == user.first_name,
        Count_model.user_last_name == user.last_name).all()

def count_by_date(db: Session, date: str) -> List[Count_model]:
    return db.query(Count_model).filter(Count_model.date == date).all()


