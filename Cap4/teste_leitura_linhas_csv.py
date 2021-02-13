import pandas as pd
    
nomeArquivo = ("arquivos/salarios.csv")

dados = pd.read_csv(nomeArquivo)

#print(dados.line_num())