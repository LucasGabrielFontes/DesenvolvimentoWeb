# Listas em python são objetos mutáveis

lista1 = [1, 2, 3]
print(id(lista1))
lista1.append(4)
print(id(lista1)) # Os endereços são os mesmos

lista2 = lista1 # As duas listas apontam para o mesmo lugar na memória
lista2.append(5) # Essa alteração afeta todas as variáveis que apontam para o mesmo lugar que lista2

print(lista1) # A lista1 também é alterada
print(lista2)