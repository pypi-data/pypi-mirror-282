import pandas as pd
import numpy as np

def exemplo_funcao(data):
    """
    Função exemplo que usa pandas e numpy.
    :param data: lista de números
    :return: DataFrame com a média e desvio padrão
    """
    df = pd.DataFrame(data, columns=["Valores"])
    media = df["Valores"].mean()
    desvio_padrao = df["Valores"].std()

    resultado = pd.DataFrame({
        "Média": [media],
        "Desvio Padrão": [desvio_padrao]
    })

    return resultado
