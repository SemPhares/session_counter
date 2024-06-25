from pydantic import BaseModel


class Count(BaseModel):
    id : str
    genre_count : str
    count: int


class Count_form(BaseModel):
    num_count : str
    nom_salle : str
    zone_count : str
    genre_count : str


class Count_db(Count_form):
    user_first_name : str
    user_last_name : str
    date : str
    time : str
    count : int