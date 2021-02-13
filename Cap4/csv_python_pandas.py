# Trabalhando com arquivo CSV no Python utilizando o pacote Pandas
import pandas as pd 

nomeArquivo = "arquivos/binary.csv"
dados = pd.read_csv(nomeArquivo)
print(dados.head())

nomeArquivo = "arquivos/salarios.csv"
dados = pd.read_csv(nomeArquivo)
print(dados.head())

print(dados.iterrows(2,2))