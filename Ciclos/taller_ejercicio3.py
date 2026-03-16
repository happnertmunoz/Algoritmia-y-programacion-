n = int(input("Ingrese un numero: "))
suma = 0
while n > 0:
    digito = n % 10
    if digito % 2 != 0:
        suma = suma + digito
    n = n // 10 
print("La suma de los digitos impares es: ",suma)