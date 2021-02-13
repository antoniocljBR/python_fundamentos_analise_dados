# Trabalhando com arquivo linha a linha

nomeArquivo = "arquivos/teste.txt"

dados = open(nomeArquivo,"r")

for linha in dados:
    print(linha)
    
dados.close()