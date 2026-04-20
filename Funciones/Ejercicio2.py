def procesar_lista(lista):
    # Caso base
    if len(lista) == 0:
        return []
    
    # Tomamos el primer elemento
    primero = lista[0]
    
    # Procesamos el resto recursivamente
    resto = procesar_lista(lista[1:])
    
    # Si es par
    if primero % 2 == 0:
        return [primero ** 2] + resto
    else:
        return resto
numeros = [1, 6, 8, 16]
print(procesar_lista(numeros))