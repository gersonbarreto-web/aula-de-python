import streamlit as st





login_salvo ="gerson"
senha_salvo = "12345"

st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)

    
usuario = st.text_input("Digite seu usuario", disabled=st.session_state.desabilitar)
senha = st.text_input("Digite sua senha: ", type= "password", disabled=st.session_state.desabilitar)


if st.button("verifica"):
    if usuario == login_salvo and senha == senha_salvo :
                st.success("seja bem vindo")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:        
            st.warning(f"senha ou usuario invalido, tentativas: {st.session_state.tentativas}")
        else:
             st.session_state.desabilitar = True      
             st.error("Numero de tentativas invalida")   