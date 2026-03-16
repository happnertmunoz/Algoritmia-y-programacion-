n = int(input("Ingrese el valor de n: "))
print("1. Cuadrados menores que n: ")
i = 0
while i * i < n:
    print(i * i, end=" ")
    i = i + 1

print()

print("2. Numeros positivos divisibles por 10 y menores que n: ")
i = 10
while i < n:
    print(i, end=" ")
    i = i + 10

print()

print("3. Potencias de dos numeros menores que n: ")
contador = 1
while contador < n:
    print(contador, end=" ")
    contador = contador * 20