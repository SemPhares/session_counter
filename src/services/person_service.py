
from sqlalchemy import or_
from sqlalchemy.orm import Session

import uuid
from fastapi import HTTPException

import security_service as security
from src.services import mail_service
from src.models.person_model import Person_model
from src.schemas.person_schema import Person_create


def get_person_by_email(db: Session, email: str):
    return db.query(Person_model).filter(Person_model.email == email).first()

def check_existing_person(db: Session, email: str):
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

    return db_user

# Créer une fonction pour vérifier les informations de connexion
def authenticate_user(db: Session, email: str, password: str):
    """
    
    """
    user = get_person_by_email(db=db,email=email)
    if user is not None and security.compareHashedText(password,user.password):
        return user
    else:
        return None

