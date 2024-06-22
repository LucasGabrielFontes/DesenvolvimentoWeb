def alteraLista(listaFunc):
    ...
    listaCopia = listaFunc[:] # Cria uma copia. Não apontaram para o mesmo lugar na memória
    listaCopia.append(4)
    print(listaCopia)
    ...

lista = [1, 2, 3]
alteraLista(lista)

print(lista)