lista1 = [1, 2, 3]
lista2 = [1, 2, 3] # Uma nova lista é criada. Não aponta para o mesmo lugar na memória que a anterior

print(id(lista1)) # Os endereços são diferentes
print(id(lista2))