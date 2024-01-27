import pandas as pd 
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para o arquivo CSV
csv_path = os.path.join(current_directory, 'BTC-USD.csv')


df = pd.read_csv(csv_path, sep=";")

colunas = {'timestamp': 'TimeStamp',
            'close' : 'Fechamento',
            'volume' : 'Volume'}

df = df.rename(columns=colunas)
colunas_selecionadas = ['TimeStamp', 'Fechamento', 'Volume']
df_formatado = df[colunas_selecionadas]

#formatando datas
df_formatado['TimeStamp'] = pd.to_datetime(df_formatado['TimeStamp'])
df_formatado['TimeStamp'] = df_formatado['TimeStamp'].dt.strftime('%Y-%m-%d')

max_fechamento = df_formatado['Fechamento'].idxmax()
row_max_fechamento = df_formatado.loc[max_fechamento]

#linha com data em que atingiu o valor máximo no período filtrado
print(row_max_fechamento)


