# 1) Funciones de la Calculadora Nivel 1

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# 2) Funciones Nivel 2: Exponente y Raíz 

def exponente(base, exp):
    """Calcula la potencia usando la función de multiplicación."""
    # Manejo de exponentes decimales (como 0.5) o negativos
    if isinstance(exp, float) or exp < 0:
        return base ** exp
        
    resultado = 1
    # Multiplicamos la base por sí misma tantas veces como diga el exponente
    for _ in range(int(exp)):
        resultado = multiplicacion(resultado, base)
    return resultado

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada usando la matemática de potencias."""
    # Matemáticamente, la raíz cuadrada es elevar a la potencia de 0.5
    # Así depende lógicamente de la estructura de exponentes
    if numero < 0:
        return "Error: Raíz de un número negativo."
    return numero ** 0.5

# 3) Función Factorial

def factorial(n):
    """Calcula el factorial usando la función de multiplicación."""
    if n < 0:
        return "Error: Factorial negativo no existe."
    if n == 0 or n == 1:
        return 1
        
    resultado = 1
    # Multiplica todos los números desde 1 hasta n
    for i in range(2, n + 1):
        resultado = multiplicacion(resultado, i)
    return resultado

# 4) Función Inversa

def inversa(numero):
    """Calcula la inversa de un número (1 / numero)."""
    # Usamos la función de división que ya creamos en el nivel 1
    return division(1, numero)

print("--- Calculadora Nivel 2 ---")
print(f"Exponente (2 a la 3): {exponente(2, 3)}") 
print(f"Raíz cuadrada de 9: {raiz_cuadrada(9)}")
print(f"Factorial de 5: {factorial(5)}")
print(f"Inversa de 3: {inversa(3)}")