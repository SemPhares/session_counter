from sqlalchemy.orm import Session

from typing import Union

import uuid
from fastapi import HTTPException

from  . import security_service as security
# from services import mail_service
from models.person_model import Person_model
from schemas.person_schema import Person_create, Person


def get_person_by_email(db: Session, email: str):
    return db.query(Person_model).filter(Person_model.email == email).first()

def check_existing_person(db: Session, email: str) -> bool:
    user = get_person_by_email(db, email)
    return user is not None


async def create_person(db: Session, person_create: Person_create):
    if check_existing_person(db, person_create.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = security.hashText(person_create.password)

    db_user = Person_model(
        id= str(uuid.uuid4()),
        email =person_create.email,
        last_name =person_create.last_name,
        first_name =person_create.first_name,
        password = hashed_password)

    db.add(db_user)
    
    db.commit()

    created_person = Person(
        last_name =person_create.last_name,
        first_name =person_create.first_name,
        email = person_create.email)

    return created_person


# Créer une fonction pour vérifier les informations de connexion
def authenticate_user(db: Session, email: str, password: str) -> Union[Person, None]:
    """
    
    """
    user = get_person_by_email(db=db,email=email)
    if user is not None and security.compareHashedText(password,str(user.password)):
        connected_person = Person(
        last_name = str(user.last_name),
        first_name = str(user.first_name),
        email = str(user.email))

        return connected_person
    else:
        return None

