def validaOpcao(posicao):
    while True:
        try:
            return float(input('Insira o ' + posicao + ' número: '))
        except ValueError:
            print("Valor inválido!")

x = validaOpcao("primeiro")
while True:
    y = validaOpcao("segundo")
    if y == 0:
        print('Valor inválido!')
    else:
        break
    

remainder = x / y
print(remainder)