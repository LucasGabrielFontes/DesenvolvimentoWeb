#lista = ["Vasco", "Gama", 5]
# Lista heterogenea
# E possivel armazenar listas dentro de listas

#lista.append("1998") # Adiciona um elemento à lista

lista = [8, 9, 5, 1, 0]

lista.append(1998)

lista.sort() # Ordena a lista
#lista.sort(reverse = True) # Ordena a lista em ordem decrescente

lista.remove(1) # Remove o elemento 1, não o elemento de indice 1
elementoRemovido = lista.pop() # Remove o ultimo elemento da lista e ainda retorna o elemento que foi removido
lista.pop(2) # Remove o elemento da posicao 2

lista.insert(3, 99) # Insere o 99 na posicao 3 da lista

for i in lista:
    print(i)

print(elementoRemovido)