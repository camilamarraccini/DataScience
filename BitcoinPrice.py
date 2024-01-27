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

print(df_formatado)


