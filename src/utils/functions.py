import streamlit as st

def check_input_is_not_empty(input):
    if input == "":
        st.error("Ce champ ne peut pas être vide")
        return input
    return ''


