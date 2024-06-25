# import streamlit as st
from schemas import person_schema
from services import person_service
from utils.functions import check_input_is_not_empty


def login_page(st, db):
    st.header("Connexion")
    login_email= check_input_is_not_empty(st.text_input("Email"))
    login_password = check_input_is_not_empty(st.text_input("Mot de passe", type="password"))
    if st.button("Se connecter"):
        # Validation des identifiants
        person_authentified = person_service.authenticate_user(db, login_email, login_password) # type: ignore

        if person_authentified:
            st.success("Connexion réussie!")
            # Redirection vers une autre page après la connexion réussie
            return person_authentified
        else:
            st.error("Identifiants incorrects. Veuillez réessayer.")
            login_page(st, db)


def create_account(st, db):
    st.header("Créer un compte")
    last_name = check_input_is_not_empty(st.text_input("Votre nom de famille"))
    first_name = check_input_is_not_empty(st.text_input("Votre prenom"))
    new_email = check_input_is_not_empty(st.text_input("Votre email nom d'utilisateur"))
    new_password = check_input_is_not_empty(st.text_input("Nouveau mot de passe", type="password"))
    if st.button("Créer un compte"):
        user_exists = person_service.check_existing_person(db, new_email) # type: ignore
        if user_exists:
            st.warning("Ce nom d'utilisateur existe déjà. Veuillez choisir un autre.")
            if st.button("Connexion avec l'utilisateur"):
                login_page(st, db)
            if st.button("Changer les informations utilisateurs"):
                create_account(st, db)
        else:
            new_person = person_schema.Person_create(last_name=last_name,
                         first_name=first_name,
                         email=new_email,
                         password=new_password)
            
            new_user = person_service.create_person(db, new_person) # type: ignore
            st.success("Compte créé avec succès!")
            return new_user


def logout(st, db):
    """
    """
    st.write("Etes-vous sûr de vouloir vous déconnecter?")
    if st.button("Yes"):
        st.session_state['connected'] = False
        st.rerun()
        login_page(st, db)
        
    else:
        st.write("You are still connected to the system.")
    