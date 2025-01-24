valores = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero %2 != 0:
        valores.append(numero)
if len(valores) == 0:
    print('Nenhum númnero ímpar')
else:
    print('Números ímpares: '+ ", ".join(map(str, valores)))
    print('Quantidade de números impares: ' + str(len(valores)))