import streamlit as st

VERMELHO_CLARO = "#ffe5e5"
AZUL_CLARO = "#e0f0ff"


def pintar_campo(chave, preenchido):
    """Pinta o fundo do campo: azul se tem valor, vermelho se está vazio."""
    cor = AZUL_CLARO if preenchido else VERMELHO_CLARO
    st.html(f"""
        <style>
        .st-key-{chave} div[data-baseweb="input"],
        .st-key-{chave} div[data-baseweb="input"] > div,
        .st-key-{chave} input,
        .st-key-{chave} button {{
            background-color: {cor} !important;
        }}
        </style>
    """)
