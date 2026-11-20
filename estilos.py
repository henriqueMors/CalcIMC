import streamlit as st

# Cores semitransparentes (rgba): o fundo do tema aparece por trás,
# então funcionam no tema claro e no escuro. O texto continua com a
# cor do próprio tema (preto no claro, branco no escuro).
VERMELHO = {"fundo": "rgba(255, 75, 75, 0.15)", "borda": "rgba(255, 75, 75, 0.6)"}
AZUL = {"fundo": "rgba(28, 131, 225, 0.15)", "borda": "rgba(28, 131, 225, 0.6)"}


def pintar_campo(chave, preenchido):
    """Pinta o campo: azul se tem valor, vermelho se está vazio."""
    cor = AZUL if preenchido else VERMELHO
    st.html(f"""
        <style>
        /* a "caixa" do campo (texto + botões - e +) recebe a cor e a borda */
        .st-key-{chave} [data-testid="stNumberInputContainer"] {{
            background-color: {cor["fundo"]} !important;
            border-color: {cor["borda"]} !important;
        }}
        /* as partes de dentro ficam transparentes para mostrar a cor da caixa */
        .st-key-{chave} [data-testid="stNumberInputContainer"] div,
        .st-key-{chave} input,
        .st-key-{chave} button {{
            background-color: transparent !important;
        }}
        </style>
    """)
