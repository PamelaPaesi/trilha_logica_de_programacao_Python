valor = 0
while valor != 10:
    try:
        valor = float(input('Insira um número: '))
        if valor == 10:
            print("Número 10! O programa será finalizado.")
            break
    except ValueError:
        print("Valor inválido!")
