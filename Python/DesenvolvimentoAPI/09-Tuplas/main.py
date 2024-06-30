tupla = (5, 6, 9) # [] Definem uma lista e () definem uma tupla (O uso de parenteses e opcional para definir uma tupla)

# Tuplas sao mais utilizadas para armazenar valores de tipos diferentes
# Listas, embora possam armazenar dados de tipos diferentes, nao sao muito utilizadas dessa forma

# E possivel criar tuplas de tuplas sem nenhum problema. Ou tuplas de lista

# As tuplas sao imutaveis!!!

#a = tupla[0]
#b = tupla[1]
#c = tupla
# Embora seja possivel, as tuplas nao sao muito utilizadas dessa maneira

a, b, c = tupla # Essa e a maneira mais utilizada (Tambem e possivel com listas)

# E comum listas de tuplas

print(a)
print(b)
print(c, "\n")

for i in tupla:
    print(i)