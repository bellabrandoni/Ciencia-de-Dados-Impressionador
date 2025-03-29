
import pandas as pd

#definimos a função tabela_distribuicao_frequencias, que cria uma tabela de distribuição de frequências para uma coluna de um DataFrame.

def tabela_distribuicao_frequencias(df, coluna, coluna_frequencia=False):

## Parâmetros:

    #df: Um DataFrame do Pandas contendo os dados.

    #coluna: Nome da coluna dentro do DataFrame que será analisada.

    #coluna_frequencia (opcional, padrão: False): False, a função calculará a frequência dos valores únicos da coluna a partir dos próprios dados.

    #Criamos um novo DataFrame vazio, df_estatistica, onde armazenaremos os cálculos estatísticos.
    df_estatistica= pd.DataFrame()

    """if coluna_frequencia for True, entendemos que df[coluna] já contém a contagem de ocorrências de cada valor.

    else: Se coluna_frequencia for False, significa que df[coluna] contém os valores brutos, então precisamos calcular a distribuição de frequências do zero:"""
    if coluna_frequencia:
        df_estatistica['frequencia'] =  df[coluna]
        df_estatistica['frequencia_relativa'] =  df_estatistica['frequencia'] /df_estatistica['frequencia'].sum()
    else:
        #Conta quantas vezes cada valor aparece na coluna.Ordena os valores em ordem crescente. Armazena na coluna frequencia.
        df_estatistica['frequencia'] =  df[coluna].value_counts().sort_index()
        #esmo cálculo de frequência, mas normalizado (normalize=True faz a divisão automática pelo total de dados). Armazena na coluna frequencia_relativa.

        df_estatistica['frequencia_relativa'] =  df[coluna].value_counts(normalize = True).sort_index()

    df_estatistica['frequencia_acumulada'] = df_estatistica['frequencia'].cumsum()
    df_estatistica['frequencia_relativa_acumulada'] = df_estatistica['frequencia_relativa'].cumsum()

    """A função retorna o DataFrame df_estatistica contendo:

    #frequencia → contagem de ocorrências de cada valor.

    #frequencia_relativa → proporção de cada valor em relação ao total.

    #frequencia_acumulada → soma progressiva das ocorrências.

    #frequencia_relativa_acumulada → soma progressiva das proporções."""
    return df_estatistica


    #Resumo da Lógica
"""Se já tivermos uma coluna de frequências (coluna_frequencia=True), apenas calculamos proporções e acumulados.

Se tivermos dados brutos (coluna_frequencia=False), primeiro contamos as ocorrências.

Sempre geramos a frequência absoluta, relativa e suas versões acumuladas."""