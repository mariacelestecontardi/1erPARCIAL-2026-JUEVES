eventos = ["Kermés", "Concurso de Comida", "Reunión del Consejo Municipal"]

def organizar_eventos(eventos, orden_descendente=False):
    if orden_descendente:
        return sorted(eventos, reverse=True)
    else:
        return sorted(eventos)

    print(organizar_eventos(eventos, True)) #Orden descendente Z -> A
    print(organizar_eventos(eventos, False)) #Orden ascendente A -> Z
    print(organizar_eventos(eventos)) #Orden ascendente A -> Z por defecto

    