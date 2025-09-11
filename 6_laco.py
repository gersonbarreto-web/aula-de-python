import streamlit as st 
import time 

st.header("contagem")

n1=st.number_input("Digite o primeiro numero: ", step=1,min_value=0)


if st.button("iniciar"):
    for i in range(n1,0,-1):
         st.warning(i)
         time.sleep(1)
