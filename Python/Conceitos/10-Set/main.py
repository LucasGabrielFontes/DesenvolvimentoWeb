# {} definem um set, um conjunto

conjunto = {1, 2, 3, 3, 3} # O 3 so e adicionado uma vez, como ja e esperado
# conjunto = set([1, 2, 3, 3, 3])

conjunto.add(4)
conjunto.add(4)
conjunto.add(0)

# O metodo set() retorna um conjunto de uma lista, por exemplo

# O conjunto e automaticamente ordenado
# E possivel comparar conjuntos com ==

print(conjunto)