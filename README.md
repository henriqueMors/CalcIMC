# Calculadora de IMC

Aplicação web feita em **Python** com **Streamlit** que calcula o Índice de Massa Corporal (IMC) e mostra a classificação do resultado.

## Funcionalidades

- Entrada de **peso** (kg) e **altura**, com escolha da unidade: **centímetros** ou **metros**
- Campos começam vazios, com dica de preenchimento (`0` para cm, `0,00` para metros)
- **Indicação visual** do preenchimento: o campo fica vermelho enquanto está vazio e azul depois de preenchido
- Botão **Calcular IMC** só é liberado quando os dois campos estão preenchidos
- Resultado com cor de acordo com a faixa:

| IMC               | Classificação     |
|---                |---                |
| abaixo de 18,5    | Abaixo do peso    |
| 18,5 a 24,9       | Peso normal       |
| 25,0 a 29,9       | Sobrepeso         |
| 30,0 ou mais      | Obesidade         |

- Compatível com os temas **claro** e **escuro** do Streamlit

## Estrutura do projeto

```
calculadora_imc/
├── app.py            # monta a página e organiza os componentes
├── componentes.py    # campos de peso e altura e exibição do resultado
├── estilos.py        # cores dos campos (CSS compatível com tema claro e escuro)
├── calculos.py       # regra de negócio: fórmula e classificação do IMC
└── test_calculos.py  # testes automatizados com pytest
```

A regra de negócio (`calculos.py`) é independente da interface: não usa Streamlit, pode ser testada isoladamente e reaproveitada em outras aplicações (API, desktop etc.).

## Como executar

```bash
# criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

# instalar as dependências
pip install streamlit pytest

# rodar o app
streamlit run app.py
```

O app abre no navegador em `http://localhost:8501`.

## Testes

```bash
pytest
```

Os testes conferem o cálculo e os limites de cada faixa de classificação (por exemplo, 18,5 já é "peso normal" e 25,0 já é "sobrepeso").

## Tecnologias

- Python 3
- Streamlit
- pytest

---

> O IMC é um indicador de referência e não substitui a avaliação de um profissional de saúde.