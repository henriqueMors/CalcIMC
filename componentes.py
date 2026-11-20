import streamlit as st

from estilos import pintar_campo


def campo_peso():
    """Campo de peso em kg. Devolve o valor ou None se vazio."""
    with st.container(key="campo_peso"):
        peso = st.number_input(
            "Digite seu peso em kg:",
            min_value=1.0,
            max_value=500.0,
            step=0.1,
            value=None,
            placeholder="0",
        )
    pintar_campo("campo_peso", peso is not None)
    return peso


def campo_altura():
    """Escolha da unidade + campo de altura. Devolve a altura em metros ou None."""
    unidade = st.radio("Opção de altura:", ("cm", "metros"))

    with st.container(key="campo_altura"):
        if unidade == "cm":
            altura = st.number_input(
                "Digite sua altura em cm:",
                min_value=1,
                max_value=300,
                step=1,
                value=None,
                placeholder="0",
            )
            altura_m = altura / 100 if altura is not None else None
        else:
            altura = st.number_input(
                "Digite sua altura em metros:",
                min_value=0.5,
                max_value=3.0,
                step=0.01,
                format="%.2f",
                value=None,
                placeholder="0,00",
            )
            altura_m = altura
    pintar_campo("campo_altura", altura is not None)
    return altura_m


def mostrar_resultado(imc, tipo, texto):
    """Mostra o resultado com a cor do alerta certa."""
    mensagem = f"Seu IMC é {imc:.2f}. {texto}"
    alertas = {"error": st.error, "info": st.info, "warning": st.warning}
    alertas[tipo](mensagem)
