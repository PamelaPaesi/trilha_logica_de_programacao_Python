while True:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    media = (nota1 + nota2) / 2

    print("Media: " +  "{:.2f}".format(media))

    if (media >= 7):
        print('Aprovado')
    else:
        print('Reprovado')

    print(" --------------------------------------------- ")
    sair = input("Deseja realizar um novo cálculo? 0 - Sim, 1 - Não : ")
    if sair == "1":
       break