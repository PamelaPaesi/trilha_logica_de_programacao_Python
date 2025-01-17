while True:
    nota1 = input('Digite a primeira nota: ')
    nota2 = input('Digite a segunda nota: ') 
    nota3 = input('Digite a terceira nota: ')

    media = (float(nota1) + float(nota2) + float(nota3)) / 3

    print("Media: " +  "{:.2f}".format(media))

    if (media >= 7):
        print('Aprovado')
    elif (media >= 5):
        print('Recuperação')
    else:
        print('Reprovado')

    print(" --------------------------------------------- ")
    sair = input("Deseja sair? 0 - Sim, 1 - Não : ")
    if sair == "0":
       break