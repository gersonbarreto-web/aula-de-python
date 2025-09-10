import streamlit as st

st.title("calculo")

numero1=st.number_input("Digite o primeiro numero")
numero2=st.number_input("Digite o segundo numero")


soma = numero1 + numero2
produto= numero1 * numero2
media =(numero1 + numero2) /2
maior= max(numero1,numero2)
menor = min(numero1, numero2)






if st.button("verificar"):
    if numero1 and numero1:
        st.write(f"soma: {soma}")
        st.write(f"produto: {produto}")
        st.write(f"media: {media}")
        st.write(f"maior:{maior}")
        st.write (f"menor:{menor}")
        
else:
    st.info("informe os numeros. ")        

