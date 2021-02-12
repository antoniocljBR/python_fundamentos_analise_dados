# Trabalhando com arquivos CSV
# Dados obtidos do site https://data.cityofchicago.org

# Quebrando o arquivo em linhas
arquivo = open("arquivos/salarios.csv","r")

dados = arquivo.read()

linhas = dados.split("\n")

print(linhas)

arquivo.close()

# Quebrando o arquivo em linhas e transformando em colunas
arquivo = open("arquivos/salarios.csv", "r")

dados = arquivo.read()

linhas = dados.split("\n")

colunas = []

count = 0
for linha in linhas:
    count += 1
    separado = linha.split(",")
    colunas.append(separado)
    
count1 = 0
for linha in linhas:
    for col in range(0,4):
        count1 += 1
        
print(colunas)
print(f"Número total de linhas: {count}")
print(f"Número total de colunas: {count1}")