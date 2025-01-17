while True:    
    produto = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    quant = input("Digite a quantidade do produto: ")
    total = float(preco) * float(quant)

    percent = 1

    if float(quant) >= 11 and float(quant) <= 20:
        percent = percent - 0.10
    else:
        if float(quant) >= 21 and float(quant) <= 50:
            percent = percent - 0.20
        else:
            if float(quant) > 50:
                percent = percent - 0.25
        
    total = total * percent

    print("Total: " +  "{:.2f}".format(total))

    print(" --------------------------------------------- ")
    sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
    if sair == "0":
        break
