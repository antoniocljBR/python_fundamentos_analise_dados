def tela_calculadora():
    print("\n******************* Python Calculator *******************\n")
    print("Informe uma das opções:\n\n")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n\n")

    opcao = input("Opção: ")
    
    return int(opcao)

def trata_opcao(selecao):
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    
    if selecao == 1:
        resultado = num1 + num2    
        print(f"\n {resultado}\n")
    elif selecao == 2:
        resultado = num1 - num2
        print(f"\n {resultado}\n")
    elif selecao == 3:
        resultado = num1 * num2
        print(f"\n {resultado}\n")
    elif selecao == 4:
        resultado = num1 / num2
        print(f"\n {resultado}\n")
    else:
        print("Opção Inválida !!!")
        
trata_opcao(tela_calculadora())