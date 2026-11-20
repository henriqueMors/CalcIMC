import streamlit as st

from calculos import calcular_imc, classificar_imc
from componentes import campo_peso, campo_altura, mostrar_resultado

st.title("Calculadora de IMC")

peso = campo_peso()
altura_m = campo_altura()

campos_preenchidos = peso is not None and altura_m is not None

if st.button("Calcular IMC", disabled=not campos_preenchidos):
    imc = calcular_imc(peso, altura_m)
    tipo, texto = classificar_imc(imc)
    mostrar_resultado(imc, tipo, texto)
