# import streamlit as st
from typing import Union
from schemas.count_shcema import Count_form
from schemas.person_schema import Person
from services.count_service import write_count_to_database

from database import get_db
db = get_db()


def increment_counter(st,
                      increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(st,
                      decrement_value=0):
    if st.session_state.count ==0:
        pass
    else:
        st.session_state.count -= decrement_value
    
def erase_counter(st):
    st.session_state.count = 0

def counter_page(st,
                 current_user: Person, 
                 count_form: Count_form):

    st.title('Compteur')

    if 'count' not in st.session_state:
        st.session_state.count = 0
        
    col1, col2 = st.columns([2, 1])
    with col1:
        
        col11, col12 = st.columns([3, 2])
        btn_container = col11.container(border=True, height=125)
        btn_container.button(':green-background[:heavy_plus_sign:]', on_click=increment_counter,
            kwargs=dict(st=st, increment_value=1), use_container_width = True)
        
        with col12:
            btn_container = st.container(border=True)

            btn_container.button(':yellow-background[:heavy_minus_sign:]', on_click=decrement_counter,
                kwargs=dict(st=st, decrement_value=1), use_container_width = True)

            btn_container.button(':black-background[:red_circle:]', 
                                 on_click=erase_counter,  kwargs=dict(st=st),
                                 use_container_width = True)


    with col2:
        display_container = st.container(border=True, height=125)
        with display_container:
            
            st.write('Count = ', st.session_state.count)
            save_count = st.button('Enregistrer le comptage', 
                            key='save_count', use_container_width = True)
            
            if save_count:
                count_ = write_count_to_database(db, # type: ignore
                                                 current_user,
                                                 count_form,
                                                 st.session_state.count)
                st.success(f"Comptage enregistré avec succès! {count_.id} {count_.genre_count} {count_.count}")
                return count_


def counter_form(st) -> Union [Count_form, None]:

    counter_container = st.container(border=True, height=400)
    with counter_container:
        # Formulaire pour entrer le numero de comptage,  le type de compatge en liste derouante, la salle en liste derouante, le nombre de personnes en entier
        num_count = st.selectbox("Sélectionnez le numero de comptage", [1, 2, 3])
        nom_salle = st.selectbox("Sélectionnez la salle", ["Salle Diamant", "Salle Or", "Auditorium"])
        zone_count = st.selectbox("Sélectionnez la zone de comptage", ["Coté droit avant", "Coté droit arriere", "Coté gauche avant", "Coté gauche arriere", "Mileu avant", "Milieu arriere"])
        genre_count = st.selectbox("Sélectionnez la type de comptage", ["Homme", "Femme", "Enfants"])
        if st.button("Valider le formulaire"):
            # ecrire en base donnée les informations du formulaire et renvoyer un id de comptage
            # Assuming you have a function called write_to_database that takes the form information as parameters
            count_form =  Count_form(
                num_count = str(num_count),
                nom_salle = str(nom_salle),
                zone_count = str(zone_count),
                genre_count = str(genre_count))
            
            return count_form
        