import streamlit as st 
import time 


st. title("laco de repeticao - for ")

st.header("contagem")


if st.button("iniciar"):
    for i in range(100,+120, 2):
         st.write(i)
         time.sleep(1)
    st.header("fim")
