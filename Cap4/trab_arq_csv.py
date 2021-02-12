# Trabalhando com arquivos CSV
# Dados obtidos do site https://data.cityofchicago.org

# Quebrando o arquivo em linhas
arquivo = open("arquivos/salarios.csv","r")

dados = arquivo.read()

linhas = dados.split("\n")

#print(linhas)

arquivo.close()

# Quebrando o arquivo em linhas e transformando em colunas
arquivo = open("arquivos/salarios.csv", "r")

dados = arquivo.read()

linhas = dados.split("\n")

colunas = []

for linha in linhas:
    separado = linha.split(",")
    colunas.append(separado)
    
print(colunas)