import pandas as pd 
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para o arquivo CSV
csv_path = os.path.join(current_directory, 'BTC-USD.csv')


df = pd.read_csv(csv_path)
print(df.head())
print(df.columns)


