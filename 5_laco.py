import streamlit as st 
import time 


st. title("calculadora ")

n1=st.number_input("Digite um numero")  
if st.button("iniciar"):
    for i in range (1,11):
        st.info(f"{n1}x{i}={n1*i}")
        time .sleep(1)
else:
    st.info("fim")