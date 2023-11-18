ordenes = []

def agregar_orden(nombre_cliente):
    orden = {"nombre_cliente": nombre_cliente, "tipo": "", "pizza": "", "bebida": ""}
    ordenes.append(orden)
    return orden
