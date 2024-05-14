import streamlit as st
from src.database import get_db, settings
from src.services import person_service
from src.schemas import person_schema

db = get_db()


def login():
    st.title("Connexion")

    # Option pour se connecter
    st.header("Se connecter")
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
                
   
def create_account():
    
    st.title("Création de compte")
    # Option pour créer un compte
    st.header("Créer un compte")
    last_name = st.text_input("Votre nom de famille")
    first_name = st.text_input("Votre prenom")
    new_email = st.text_input("Votre email nom d'utilisateur")
    new_password = st.text_input("Nouveau mot de passe", type="password")
    if st.button("Créer un compte"):
        user_exists = person_service.check_existing_person(db, new_email)
        if user_exists:
            st.error("Ce nom d'utilisateur existe déjà. Veuillez choisir un autre.")
        else:
            new_person ={'last_name': last_name,
                         'first_name': first_name,
                         'email': new_email,
                         'password': new_password}
            
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


# Fonction de connexion à la base de données PostgreSQL
# def connect_to_db():
#     import psycopg2
#     conn = psycopg2.connect(
#         dbname='counter_db',
#         user='counter_user',
#         password='counter_password',
#         host='postgres',  # Nom du service dans le conteneur Docker
#         port='5432'
#     )
#     return conn

# # Fonction de validation de l'existence d'un utilisateur
# def user_exists(username):
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#     user = cursor.fetchone()
#     cursor.close()
#     conn.close()
#     return user is not None

# # Fonction de validation de l'existence d'un utilisateur
# def valide_user_exists(username):
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#     user = cursor.fetchone()
#     cursor.close()
#     conn.close()
#     return user is not None

# # Fonction de création de compte
# def create_account(username, password):
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
#     conn.commit()
#     cursor.close()
#     conn.close()


# Lancer l'application
# if __name__ == "__main__":
#     login


# import streamlit as st
# from streamlit_authenticator import Auth

# # Création d'une instance d'Authenticator
# authenticator = Auth(
#     authentication_methods=["password"],
#     db_connection=f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}")

# # Page de connexion et de création de compte
# def login_or_create_account_page():
#     st.title("Connexion")

#     # Vérifie si l'utilisateur est connecté
#     if authenticator.user is None:
#         # Affiche le formulaire de connexion
#         login_result = authenticator.login_form()
#         if login_result is not None:
#             st.success("Connexion réussie!")
#             # Redirection vers une autre page après la connexion réussie
#     else:
#         st.success("Vous êtes déjà connecté en tant que " + authenticator.user)
#         st.button("Se déconnecter", on_click=authenticator.logout)

# # Lancer l'application
# if __name__ == "__main__":
#     login_or_create_account_page()
