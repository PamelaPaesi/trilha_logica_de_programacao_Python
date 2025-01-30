def validaopcao(posicao):
    while True:
        try:
            return float(input('Insira o ' + posicao + ' número: '))
        except ValueError:
            print("Valor inválido!")

def primeironro(ultnro):
    while True:
        if ultnro > 0: 
            sair = input("Deseja manter o último resultado ("+str(ultnro)+")? 0 - Sim, 1 - Não : ")
        else:
            sair = "1"
        match sair:
            case "0": # Sim
                return ultnro
            case "1": # Não
                nro = validaopcao("primeiro")
                return nro
            case _:
                print("Operação inválida!")
                print("---------------------")
                sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
                if sair == "0":
                    break

def segundonro():
    nro = validaopcao("segundo")
    return nro

result = 0
while True:
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    operacao = input('Escolha uma das operações acima:  ')
    match operacao:
        case "1": # Somar
            result = primeironro(result) + segundonro()
        case "2": # Subtrair
            result = primeironro(result) - segundonro()
        case "3": # Multiplicar
            result = primeironro(result) * segundonro()
        case "4": # Dividir
            n1 = primeironro(result) 
            n2 = segundonro()
            if(n1 == 0 or n2 == 0):
                print("Divisão por 0 não é permitida")
                result = 0
            else:
                result = primeironro(result) / segundonro()
        case _:
            print("Operação inválida!")
            print("---------------------")
            sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
            if sair == "0":
                break
    print("Resultado da operação é: ", result)
    print(" --------------------------------------------- ")
    sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
    if sair == "0":
        break