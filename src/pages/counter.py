import streamlit as st

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

col1, col2 = st.columns(2)

with col1:
    
    btn_container = st.container(border=True)

    btn_container.button(':green-background[:heavy_plus_sign:]', on_click=increment_counter,
        kwargs=dict(increment_value=1))

    btn_container.button(':yellow-background[:heavy_minus_sign:]', on_click=decrement_counter,
        kwargs=dict(decrement_value=1))

    btn_container.button(':black-background[:red_circle:]', on_click=erase_counter)

with col2:
    with st.container(border=True):
        st.write('Count = ', st.session_state.count)