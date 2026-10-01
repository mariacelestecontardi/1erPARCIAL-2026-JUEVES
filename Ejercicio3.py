a = int(input("Ingrese la cantidad de interrupciones por hora:"))
b = int(input("Ingrese la cantidad de horas de la tarde:"))

def calcular_cantidad_interrupciones(a,b):
    if b == 0:
        return 0
    
    else:
        return a + calcular_cantidad_interrupciones(a, b - 1)

total = calcular_cantidad_interrupciones(a,b)

if total == 0:
    print("No hay interrupciones")
else:
    print("El total de interrupciones fue:", total)
    
