import streamlit as st

st.title("logica de programacao")

st.header("laco de repeticao - for")


soma = 0 

for i in range(4):
    nota = st.number_input(f"digite a {i+1}ªnota:")
    soma = soma + nota 

media = soma / 4

if st.button("Mostrar resultado"):
    st.info(f"media: {media}")
