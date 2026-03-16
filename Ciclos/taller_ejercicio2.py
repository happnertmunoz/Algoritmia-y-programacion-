suma = 0
i = 2 
while i <= 100:
    suma = suma + 1
    i = i + 2
print("1. Suma de los numeros pares entre 2 y 100: ", suma)

print()

suma = 0
i = 1
while i <= 100:
    suma = suma + (i * i)
    i = i + 1
print("2. Suma de los cuadrados entre 1 y 100:", suma)

print()

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
suma = 0
i = a
while i <= b:
    if i % 2 != 0:
        suma = suma + i
    i = i + 1
print("3. Suma de los numeros impares entre a y b: ", suma)

print()

n = int(input("Ingrese un numero: "))
suma = 0
while n > 0:
    digito = n % 10
    if digito % 2 != 0:
        suma = suma + digito
    n = n // 10 
print("La suma de los digitos impares es:", suma)