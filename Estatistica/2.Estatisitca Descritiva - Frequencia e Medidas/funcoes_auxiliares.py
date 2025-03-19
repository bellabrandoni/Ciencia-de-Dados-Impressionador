
import pandas as pd

#criando função de distribuição de frequencias 

def tabela_distribuicao_frequencias(df, coluna):
    df_estatistica= pd.DataFrame()

    df_estatistica['frequencia'] =  df[coluna].value_counts().sort_index()
    df_estatistica['frequencia_relativa'] =  df[coluna].value_counts(normalize = True).sort_index()
    df_estatistica['frequencia_acumulada'] = df_estatistica['frequencia'].cumsum()
    df_estatistica['frequencia_relativa_acumulada'] = df_estatistica['frequencia_relativa'].cumsum()

    return df_estatistica
    