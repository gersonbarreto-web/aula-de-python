import streamlit as st





login_salvo ="gerson"
senha_salvo = "12345"


usuario = st.text_input("Digite seu usuario")
senha = st.text_input("Digite sua senha: ", type= "password")

if st.button("verifica"):

        if usuario == login_salvo and senha == senha_salvo :
                st.success("seja bem vindo")

        else:
                st.error("senha ou usuario invalido")  
        

      