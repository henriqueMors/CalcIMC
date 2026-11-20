import streamlit as st

peso = st.number_input("Digite seu peso em kg:", min_value=1.0, max_value=500.0, step=0.1)

status = st.radio("Opção de altura:", ("cm", "metros"))
if (status == "cm"):
    altura = st.number_input(
        "Digite sua altura em cm:", 
        min_value=1.0, 
        max_value=300.0, 
        step=0.1
    )
    try:
        imc = peso / ((altura / 100) ** 2)
    except ZeroDivisionError:
        st.error("Erro: A altura não pode ser zero.")
else:
    altura_metros = st.number_input(
        "Digite sua altura em metros:", 
        min_value=0.5, 
        max_value=3.0, 
        step=0.01
    )
    try:
        imc = peso / (altura_metros ** 2)
    except ZeroDivisionError:
        st.error("Erro: A altura não pode ser zero.")
        
if (st.button("Calcular IMC")):
    if (imc < 18.5):
        st.error(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
    elif (imc >= 18.5 and imc < 25):
        st.info(f"Seu IMC é {imc:.2f}. Você está com o peso normal.")
    elif (imc >= 25 and imc < 30):
        st.warning(f"Seu IMC é {imc:.2f}. Você está com sobrepeso.")
    else:
        st.error(f"Seu IMC é {imc:.2f}. Você está com obesidade.")