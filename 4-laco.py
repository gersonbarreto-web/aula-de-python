import streamlit as st 
import time 

st.title("verificado pares e impares")

pares = 0
impares = 0

for i in range(1,6):
    numero= st.number_input(f"digite o {i}º numero: ", step=1)
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

if st.button("Verificar"):
    st.info(f"Quantidade de pares: {pares}") 
    st.info(f"Quantidade de impares: {impares}")   