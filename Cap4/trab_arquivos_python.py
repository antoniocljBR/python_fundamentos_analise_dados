# Trabalhando com arquivos em python

nomeArquivo = input("Entre com o nome para o arquivo: ")

nomeArquivo = nomeArquivo + ".txt"

arquivo = open(nomeArquivo,"w")

arquivo.write("Realizando teste de gravação")

arquivo.close()

arquivo = open(nomeArquivo,"r")

print(arquivo.read())
