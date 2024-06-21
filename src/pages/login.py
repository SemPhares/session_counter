import streamlit as st
from src.database import get_db
from config import Settings

from src.services import person_service
from src.schemas import person_schema

db = get_db()
settings = Settings()


def login():
    st.header("Connexion")
    login_email= st.text_input("Email")
    login_password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        # Validation des identifiants
        authentified = person_service.authenticate_user(db, login_email, login_password)
        if authentified:
            st.success("Connexion réussie!")
            # Redirection vers une autre page après la connexion réussie
        else:
            st.error("Identifiants incorrects. Veuillez réessayer.")
            if st.button("Cliquez ici pour Créer un compte"):
                create_account()
                
def check_input_is_not_empty(input):
    if input == "":
        st.error("Ce champ ne peut pas être vide")
        return input
    return ''


def create_account():
    st.header("Créer un compte")
    last_name = check_input_is_not_empty(st.text_input("Votre nom de famille"))
    first_name = check_input_is_not_empty(st.text_input("Votre prenom"))
    new_email = check_input_is_not_empty(st.text_input("Votre email nom d'utilisateur"))
    new_password = check_input_is_not_empty(st.text_input("Nouveau mot de passe", type="password"))
    if st.button("Créer un compte"):
        user_exists = person_service.check_existing_person(db, new_email)
        if user_exists:
            st.error("Ce nom d'utilisateur existe déjà. Veuillez choisir un autre.")
        else:
            new_person = person_schema.Person_create(last_name=last_name,
                         first_name=first_name,
                         email=new_email,
                         password=new_password)
            
            user = person_service.create_person(db, new_person)
            st.success("Compte créé avec succès! Vous pouvez maintenant vous connecter.")


# Page de connexion ou de création de compte Streamlit
st.header("Bienvenue sur notre compteur")
col1, col2 = st.columns(2)

with col1:
    
    if st.button("Cliquez ici pour vous connecter"):
        login()

with col2:
    
     if st.button("Cliquez ici pour vous créer un compte"):
        create_account()
