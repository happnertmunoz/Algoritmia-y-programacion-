A = float(input("Ingrese el primer numero: "))
B = float(input("Ingrese el segundo numero: "))
simbolo = input("Ingrese la operacion (+, -, *, /) : ") 
if simbolo == "+":
    resultado = A + B 
    print("Resultado =", resultado)
elif simbolo == "-":
    resultado = A - B
    print("Resultado =", resultado)
elif simbolo == "*":
    resultado = A * B 
    print("Resultado =", resultado)
elif simbolo == "/":
    if B != 0:
        resultado = A / B
        print("Resultado =", resultado)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Error: Simbolo no valido")