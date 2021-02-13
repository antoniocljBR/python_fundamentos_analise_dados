import os
import csv

texto = "Cientista de dados é a profissão que mais tem crescido em todo o mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, Big Data"

arquivo = open(os.path.join("arquivos/cientista.txt"),"w")

for palavra in texto.split():
    arquivo.write(palavra+' ')
    
arquivo.close()

# Lendo o arquivo

arquivo = open("arquivos/cientista.txt","r")
dados = arquivo.read()
arquivo.close()

print(dados)

with open("arquivos/cientista.txt","r") as arquivo:
   dados =  arquivo.read()
   arquivo.close()
   
print(dados)

with open("arquivos/cientista.txt","w") as arquivo:
    arquivo.write(texto[:21])
    arquivo.write("\n")
    arquivo.write(texto[:33])
    
with open("arquivos/cientista.txt","r") as arquivo:
   dados =  arquivo.read()
   arquivo.close()
   
print(dados)

# Excrevendo arquivo CSV
with open("arquivos/dados_csv.csv","w") as arquivo:
    escrita = csv.writer(arquivo)
    escrita.writerow(["Nome","Endereço","Cidade","Estado"])
    escrita.writerow(["Antonio","Rua dos Crisantemos, 1212","Alfafas","RS"])
    
# Lendo arquivo CSV
with open("arquivos/dados_csv.csv","r") as arquivo:
    leitura = csv.reader(arquivo)
    dados = list(leitura)
    
print(dados)