nomes = []

for i in range(10):
    nomes.append(input("Digite um nome: "))
while True:
    print(" --------------------------------------------- ")
    novo_nome = (input("Informe outro nome: "))
    if novo_nome in nomes:
        print('Achei')
    else:
        print('Não achei')
    print(" --------------------------------------------- ")
    sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
    if sair == "0":
        break