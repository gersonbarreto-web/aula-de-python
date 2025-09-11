import streamlit as st 
import time 


st. title("laco de repeticao - for ")

st.header("contagem")

if st.button("iniciar"):
    for i in range(1,21,2):
         st.info(i)
         time.sleep(1)
    st.header("fim")
