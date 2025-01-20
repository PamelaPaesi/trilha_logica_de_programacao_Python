while True: 
    nome = input("Digite o nome do vendedor: ")
    valor = float(input("Digite o valor do imóvel: "))


    if valor >= 50000:
        percent = 0.20
    elif valor >= 30000:
        percent = 0.15
    else:
        percent = 0.10

    print("Vendedor: " + nome + " Valor do imóvel: " + str(valor) + " Valor da comissão: " "{:.2f}".format(valor * percent))

    print(" --------------------------------------------- ")
    sair = input("Deseja cadastrar mais uma venda? 0 - Sim, 1 - Não : ")
    if sair == "0":
        break