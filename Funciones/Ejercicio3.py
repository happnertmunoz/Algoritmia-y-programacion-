def suma_recursiva(lista):
    # Caso base
    if not lista:
        return 0
    
    # Caso recursivo
    return lista[0] + suma_recursiva(lista[1:])
numeros = [1, 2, 3, 4, 5]
print(suma_recursiva(numeros))