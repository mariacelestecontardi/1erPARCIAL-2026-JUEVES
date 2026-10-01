a = int(input("Ingrese la cantidad de donas consumidas por persona:"))
b = int(input("Ingrese la cantidad de personas:"))

def calcular_total_donas(a,b):
    total = 0

    for i in range(b):
        total = total + a

    return total

print("El total de donas consumidas es:", calcular_total_donas(a,b))
