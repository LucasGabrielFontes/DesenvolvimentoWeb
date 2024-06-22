# Cuidado com os efeitos colateráis em Python!!!!!!!!!!!!!!

notas = [10, 9, 8.5]
notasOrdenadas = sorted(notas) # Não apontarão para o mesmo lugar. Apenas notasOrdenadas estará ordenada

print(id(notas) == id(notasOrdenadas)) # False

print(notas)
print(notasOrdenadas)