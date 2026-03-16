n = int(input("Ingrese un numero: "))
factor = 2
while n > 1:
    if n % factor == 0:
        print(factor)
        n = n // factor
    else:
        factor = factor + 1