import pytest

from calculos import calcular_imc, classificar_imc


def test_calcular_imc():
    assert calcular_imc(80, 1.75) == pytest.approx(26.12, abs=0.01)


@pytest.mark.parametrize("imc, esperado", [
    (17.0, "error"),    # abaixo do peso
    (18.5, "info"),     # limite: já é normal
    (24.9, "info"),
    (25.0, "warning"),  # limite: já é sobrepeso
    (29.9, "warning"),
    (30.0, "error"),    # obesidade
])
def test_classificar_imc(imc, esperado):
    tipo, _ = classificar_imc(imc)
    assert tipo == esperado
