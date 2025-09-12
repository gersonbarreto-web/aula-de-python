import streamlit as st

st.title("logica de programacao")

st.header("laco de repeticao - for ")

qauntidade_notas = 3
soma = 0

for i in range(qauntidade_notas):
    nota + st.number_input(f"digite a {i+1}ªnota :")
    soma = soma + nota 
                        
media = soma / qauntidade_notas

if st.button("mostra resultado"):
    st.info(F"media:{media:.1f}")
    if media >=7:
        st.success(f"aprovado")
    elif media >=4:
        st.warning(f"recuperacao")
    else:
        st.error(f"reprovado")        

