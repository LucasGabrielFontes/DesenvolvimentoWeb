notas = [10, 9, 8.5]
notasOrdenadas = notas # Apontarão para o mesmo lugar na memória

print(id(notas) == id(notasOrdenadas))

notasOrdenadas.sort() # A lista notas também será ordenada

print(notasOrdenadas)
print(notas)