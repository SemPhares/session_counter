from pydantic import BaseModel, EmailStr


class Person(BaseModel):
    last_name: str
    first_name: str
    email: EmailStr


class Person_create(Person):
    password : str
