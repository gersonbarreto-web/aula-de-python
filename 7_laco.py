import streamlit as st 

n1=st.number_input("Digite o 1 numero")
n2=st.number_input("Digite o 2 numero")
n3=st.number_input("Digite o 3 numero")
n4=st.number_input("Digite o 4 numero")
n5=st.number_input("Digite o 5 numero")

soma= n1 +n2 + n3 + n4 + n5 

if st.button("soma"):
    if n1 and n2 and n3 and n4 and n5 :
        st.write(f"soma: {soma}")
else:
    st.info("informe os numeros")



