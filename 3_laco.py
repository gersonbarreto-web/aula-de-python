import streamlit as st

st.title("verifique sua  media ")

media = st.number_input ("digite sua media  ")

if st.button("verifica"):
    if media >=7:
        st.success("aprovado")
    else:
        st.error("reprovado")

else:
    st.info("Por favor, digite a sua media ")

#success - verde
#waring - amarelo
#info - azul
#error - vermelhor