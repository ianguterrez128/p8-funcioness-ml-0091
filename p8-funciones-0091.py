# 6 ejemplos de El Pythonista
# ian gutierrez NC = 0091

# 1. Función sin parámetros 
# El Pythonista

def saludar():
    print("Hola, mundo")

saludar()

# 2. Función con parámetros

def sumar(a, b):
    return a + b

print(sumar(5, 3))

# 3. Función con parámetros por nombre

def presentar(nombre, edad):
    print(nombre, edad)

presentar(nombre="Ian", edad=17)

# 4. Función con valor predeterminado

def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar("Ian"))

# 5. Función que devuelve varios valores

def calcular(a, b):
    return a + b, a - b

suma, resta = calcular(8, 3)
print(suma, resta)

# 6. Función para comprobar si un número es par

def es_par(numero):
    return numero % 2 == 0

print(es_par(4))

# programa realizado por ian gutierrez NC = 0091
print("programa realizado por ian gutierrez NC = 0091")