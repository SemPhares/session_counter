import streamlit as st
from utils.st_modal import Modal 


st.title('Compteur')

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    if st.session_state.count ==0:
        pass
    else:
        st.session_state.count -= decrement_value
    
def erase_counter():
    st.session_state.count = 0

count_modal = Modal("Comptage enregistré", key="count_modal", padding=20, max_width=744)

counter_container = st.container(border=True, height=350)
with counter_container:
    # Formulaire pour entrer le numero de comptage,  le type de compatge en liste derouante, la salle en liste derouante, le nombre de personnes en entier
    num_count = st.selectbox("Sélectionnez le numero de comptage", [1, 2, 3])
    nom_salle = st.selectbox("Sélectionnez la salle", ["Salle Diamant", "Salle Or", "Auditorium"])
    zone_count = st.selectbox("Sélectionnez la zone de comptage", ["Coté droit avant", "Coté droit arriere", "Coté gauche avant", "Coté gauche arriere", "Mileu avant", "Milieu arriere"])
    genre_count = st.selectbox("Sélectionnez la type de comptage", ["Homme", "Femme", "Enfants"])


col1, col2 = st.columns([2, 1])
with col1:
    
    col11, col12 = st.columns([3, 2])
    btn_container = col11.container(border=True, height=125)
    btn_container.button(':green-background[:heavy_plus_sign:]', on_click=increment_counter,
        kwargs=dict(increment_value=1), use_container_width = True)
    
    with col12:
        btn_container = st.container(border=True)

        btn_container.button(':yellow-background[:heavy_minus_sign:]', on_click=decrement_counter,
            kwargs=dict(decrement_value=1), use_container_width = True)

        btn_container.button(':black-background[:red_circle:]', on_click=erase_counter, use_container_width = True)


with col2:
    display_container = st.container(border=True, height=125)
    with display_container:
        
        st.write('Count = ', st.session_state.count)
        save_count = st.button('Enregistrer le comptage', 
                           key='save_count', use_container_width = True)

if save_count:
    count_modal.open(rerun_condition = False)
    if count_modal.is_open():
        with count_modal.container():
            st.write(f'Salle {nom_salle}')
            st.write(f'Zone {zone_count}')
            st.write(f'Comptage numero {num_count}')
        count_modal.close(rerun_condition=False)


                    