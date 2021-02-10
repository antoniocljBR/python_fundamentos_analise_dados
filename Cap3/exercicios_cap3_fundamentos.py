# Data Science Academy - Python Fundamentos - Capítulo 3
# Download: https://github.com/antoniocljBR/python_fundamentos_analise_dados.git

# Exercícios Cap03

# Exercícios - Loops e Condiconais

# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
diaSemanal = input("Informe o dia da semana (segunda, terça, quarta, quinta, sexta, sábado, domingo): ")

if diaSemanal.lower() == "sábado" or diaSemanal.lower() == "domingo":
    print("Hoje é dia de descanso")
else:
    print("Vocé precisa trabalhar!")

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
frutas = ["Laranja", "Abacaxi", "Melão", "Morango", "Uva", "Maçã", "Pêssego"]

for i in frutas:
    if i == "Morango":
        print("Temos Morango !!!")

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
tupla = (21,34,56,78)

lista = []
for i in tupla:
    lista.append(i*2)

print(lista)
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')
    
    

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."