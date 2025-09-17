import streamlit as st

st.title("laco de repeticao")

st.write("escreva um algoritmo")

nota1 = st.number_input("digite a primeira nota:", min_value=0, max_value=10)
nota2 = st.number_input("digite a segunda nota ", min_value=0, max_value=10)

media = (nota1 + nota2) / 2

if st.button("calcular media "):
    st.info(f"media {media}")



