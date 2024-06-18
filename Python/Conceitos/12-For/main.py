notas = {
    "Lucas": 10,
    "Cristiano Ronaldo": 7,
    "Messi": 9.9
}

# O for in pode ser usados em estruturas de dados iteraveis: dicionarios, conjuntos, listas e tuplas

# Metodos muito uteis em dicionarios:
# dicionario.keys() retorna uma estrutura iteravel sobre as chaves dos valores
# dicionario.items() retorna uma estrutura iteravel sobre todo o dicionario
# dicionario.values() retorna uma estrutura iteravel sobre os valores do dicionario

for i in notas.keys():
    print(i)

print("\n")

for i in notas.values():
    print(i)

print("\n")

for i in notas.items():
    print(i)

print("\n")

for i, j in notas.items(): # Trabalha com as chaves e os valores ao mesmo tempo
    print(i, ": ", j, sep = "")