# Na pratica, uma matriz
lista = [
    ["Vasco", "Gama"],
    ["Python", "Java", "C++"]
]

tamLista = len(lista) # Retorna o tamanho da lista

i = 0
while (i < tamLista):
    j = 0
    tamSublista = len(lista[i])
    while (j < tamSublista):
        print(lista[i][j])
        j += 1
    i+= 1

print("\n")

# Maneira bem melhor:
for i in lista:
    for j in i:
        print(j)