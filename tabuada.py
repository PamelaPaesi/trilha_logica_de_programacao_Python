def calculaTabuada(tabuada):
    for i in range(11):
        if i > 0:
            print(str(tabuada) + " x " + str(i) + " = " + str(tabuada*i))  

tabuadas = [1,2,3,4,5,6,7,8,9,10]

while True:
    try:
        tabuada = int(input('Escolha a Tabuada a ser calculada: '))
        if tabuada in tabuadas:
            calculaTabuada(tabuada)
            break
        else:
            print("Valor inválido!")
    except ValueError:
        print("Valor inválido!")
    