# import sys, os
# sys.path.insert(0,os.getcwd())    

import streamlit as st
from mypages.login import login_page, create_account, logout
from mypages.counter import counter_page, counter_form
from database import get_db
db = get_db()

st.set_page_config(
    page_title="Hello",
    page_icon="👋")

st.session_state['connected'] = True
from schemas.person_schema import Person
st.session_state['current_user'] = Person(
        last_name = str("EGLOH LOKOH"),
        first_name = str("Sem"),
        email = str("sem.eglohlokoh@gmail.com"))

if not st.session_state['connected']:
    with st.container():
        # Page de connexion ou de création de compte Streamlit
        st.header("Binvenue sur le compteur de l'EDJ! 👋")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Cliquez ici pour vous connecter"):
                person_authentified = login_page(st, db) 
                if person_authentified:
                    st.session_state['connected'] = True
                    st.session_state['current_user'] = person_authentified
    
        with col2:
            if st.button("Cliquez ici pour vous créer un compte"):
                new_user = create_account(st, db) 
                if new_user:
                    st.session_state['connected'] = True
                    st.session_state['current_user'] = new_user

else:
       
    st.write(f"Bienvenue {st.session_state['current_user'].first_name} {st.session_state['current_user'].last_name}!")
    st.success("Vous êtes connecté(e)!", icon="✅")

    count_form = counter_form(st)
    if count_form:
        count_ = counter_page(st,
                              st.session_state['current_user'], 
                              count_form)
        if count_:
             st.success("Merci d'avoir utilisé notre application! 👋")

        # refaire un autre compatge
        if st.button("Refaire un autre comptage"):
            st.session_state.count = 0
            st.rerun()

    # Déconnexion
    with st.sidebar:
        user_container = st.container(border=True)
        with user_container:
            st.write(f"🥳 Hello {st.session_state['current_user'].first_name}")
            st.button("Se déconnecter", on_click=logout, kwargs=dict(st=st, db=db))