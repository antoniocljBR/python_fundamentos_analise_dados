# Data Science Academy - Python Fundamentos - Capítulo 2
# Download: https://github.com/antoniocljBR/python_fundamentos_analise_dados.git

# Exercícios Cap02

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = []
for i in range(1,11):
    lista.append(i)
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista = [1,2,3,4,5]

print(lista)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
str1 = "Antonio Carlos"
str2 = "Lemos Júnior"
str3 = str1 + " " + str2
print(str3)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
tupla.count(4)

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict = []
print(dict)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict = {0:"Desligado", 1:"Ligado", 2:"Quebra de fio"}
for i in dict:
    print(dict[i])

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict = {0:"Desligado", 1:"Ligado", 2:"Quebra de fio"}
dict.update({3:"Fora de range"})
print(dict)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dict = {0:"Desligado",1:"Ligado","binario":{1,2}}
print(dict)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista = ["Estado",("Binário","Indeterminado"),{0:"Desligado",1:"Ligado"},10.3]
print(lista)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:18])