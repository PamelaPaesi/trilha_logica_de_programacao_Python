nomes = []

for i in range(20):
    nomes.append(input("Digite um nome: "))
print(" --------------------------------------------- ")
nomesUnique = []
for nome in nomes:
    if nome not in nomesUnique:
        nomesUnique.append(nome)
print(", ".join(map(str, nomesUnique)))

   