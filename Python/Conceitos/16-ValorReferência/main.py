x = 10
y = 10

print(id(10))
print(id(x)) # Os endereços são exatamente os mesmos
print(id(y))

# 10 é um objeto inteiro. x e y são variáveis que apontam para ele. Auxílio na economia de memória
# Quando há um objeto sem nenhuma referência apontando para ele, ocorre uma limpeza de lixo do python