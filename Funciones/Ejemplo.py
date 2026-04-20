
def resta(a,b):
    print(a-b)

resta(1,2)

###Calculadora

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def division(a,b):
    return a/b

def multi(a,b):
    return a*b

a = 4
b = 8

print(suma(a,b))

###Fibonacci

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    

print(Fibonacci(10))