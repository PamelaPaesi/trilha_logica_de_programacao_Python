def validaOpcao(posicao):
    while True:
        try:
            return float(input('Insira o ' + posicao + ' número: '))
        except ValueError:
            print("Valor inválido!")

def primeiroNro(UltNro):
    while True:
        if UltNro > 0: 
            sair = input("Deseja manter o último resultado ("+str(UltNro)+")? 0 - Sim, 1 - Não : ")
        else:
            sair = "1"
        match sair:
            case "0": # Sim
                return UltNro
            case "1": # Não
                nro = validaOpcao("primeiro")
                return nro
            case _:
                print("Operação inválida!")
                print("---------------------")
                sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
                if sair == "0":
                    break

def segundoNro():
    nro = validaOpcao("segundo")
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
            result = primeiroNro(result) + segundoNro()
        case "2": # Subtrair
            result = primeiroNro(result) - segundoNro()
        case "3": # Multiplicar
            result = primeiroNro(result) * segundoNro()
        case "4": # Dividir
            result = primeiroNro(result) / segundoNro()
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