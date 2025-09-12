import streamlit as st


st.title("laco de repeticao - while")

nota= st.number_input("digite uma nota: ", step=1)

if st.button("verificar"):
    if nota < 0 or nota > 10:
        st.warning(" A nota deve ser entre 0 e 10.")
    else:
        st.info(f"nota:{nota}")    