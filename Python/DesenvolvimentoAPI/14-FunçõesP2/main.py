def fatorial(num):
    if (num == 0):
        return 1
    else:
        return num * fatorial(num-1)
    
n = int(input("Calcular o fatorial de: "))

while (n < 0):
    n = int(input("Valor inválido. Tente novamente: "))

fat = fatorial(n)

print("Fatorial de ", n, ": ", fat, sep="")