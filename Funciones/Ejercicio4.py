def invertir_cadena(texto):
    if not texto:
        return ""
    
    return texto[-1] + invertir_cadena(texto[:-1])
print(invertir_cadena("hola"))