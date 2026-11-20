# Regras de negócio puras: sem Streamlit, fáceis de testar com pytest


def calcular_imc(peso, altura_m):
    """Calcula o IMC com o peso em kg e a altura em metros."""
    return peso / (altura_m ** 2)


def classificar_imc(imc):
    """Devolve (tipo do alerta, texto da classificação)."""
    if imc < 18.5:
        return "error", "Você está abaixo do peso."
    elif imc < 25:
        return "info", "Você está com o peso normal."
    elif imc < 30:
        return "warning", "Você está com sobrepeso."
    else:
        return "error", "Você está com obesidade."
