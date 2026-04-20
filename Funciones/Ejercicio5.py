def max_recursivo(lista):
    # Caso base
    if len(lista) == 1:
        return lista[0]
    
    max_del_resto = max_recursivo(lista[1:])
    
    if lista[0] > max_del_resto:
        return lista[0]
    else:
        return max_del_resto
numeros = [3, 7, 2, 9, 5]
print(max_recursivo(numeros))