while True:    
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quant = int(input("Digite a quantidade do produto: "))
    total = preco * quant

    percent = 1

    if 11 <= quant <= 20:
        percent = percent - 0.10
    else:
        if 21 <= quant <= 50:
            percent = percent - 0.20
        else:
            if quant > 50:
                percent = percent - 0.25
        
    total = total * percent

    print("Total: " +  "{:.2f}".format(total))

    print(" --------------------------------------------- ")
    sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
    if sair == "0":
        break
